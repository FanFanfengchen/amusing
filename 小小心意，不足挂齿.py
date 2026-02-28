import time
from turtle import *
from datetime import datetime, timedelta
import threading
import asyncio
import math  # 移动到这里
import random  # 移动到这里
from pygame.math import Vector2
import pygame

# =======================================================================================================================
# 计分

# 窗口配置
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

# 游戏参数
game_duration = 60  # Duration in seconds
player_base_speed = 20
acceleration_factor = 1.8
ball_radius = 20
rebound_coefficient = 0.85
collision_force = 28
blue_ball_acceleration = 0.99
blue_ball_max_speed = 25
acceleration_threshold = 27  # Frame count, about 0.45 second
PLAYER_SIZE = 50  # Player size
SCORE_SMALL = 0.5  # Small collision score
SCORE_LARGE = 1.0  # Large collision score

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
# Use Chinese font (ensure the system has SimHei font)
font = pygame.font.SysFont("SimHei", 36)
larger_font = pygame.font.SysFont("SimHei", 72, bold=True)

# Game state
game_running = False
start_time = 0
score = 0

# Game objects
player = pygame.Rect(750, 750, 50, 50)
blue_ball_pos = Vector2(750, 750)
blue_ball_velocity = Vector2()
yellow_ball_pos = Vector2(SCREEN_WIDTH // 2, 200)
yellow_ball_velocity = Vector2(3, 0)

# Key timers
key_timer = {pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0}


def reset_game():
    global player, blue_ball_pos, blue_ball_velocity
    global yellow_ball_pos, yellow_ball_velocity, score
    global start_time, game_running
    player = pygame.Rect(750, 750, 50, 50)
    blue_ball_pos = Vector2(750, 750)
    random_angle = math.radians(random.uniform(0, 360))
    blue_ball_velocity = Vector2(15 * math.cos(random_angle), 15 * math.sin(random_angle))
    yellow_ball_pos = Vector2(SCREEN_WIDTH // 2, 200)
    yellow_ball_velocity = Vector2(3, 0)
    score = 0
    start_time = pygame.time.get_ticks()
    game_running = True


def detect_collision(rect, circle_pos, radius):
    closest_x = max(rect.left, min(circle_pos.x, rect.right))
    closest_y = max(rect.top, min(circle_pos.y, rect.bottom))
    dx = circle_pos.x - closest_x
    dy = circle_pos.y - closest_y
    return dx ** 2 + dy ** 2 < radius ** 2


def ball_collision_detection(pos1, pos2, radius):
    return pos1.distance_to(pos2) < radius * 2


def handle_boundary(position, velocity, radius):
    if position.x < radius:
        position.x = radius
        velocity.x = abs(velocity.x) * rebound_coefficient
    elif position.x > SCREEN_WIDTH - radius:
        position.x = SCREEN_WIDTH - radius
        velocity.x = -abs(velocity.x) * rebound_coefficient

    if position.y < radius:
        position.y = radius
        velocity.y = abs(velocity.y) * rebound_coefficient
    elif position.y > SCREEN_HEIGHT - radius:
        position.y = SCREEN_HEIGHT - radius
        velocity.y = -abs(velocity.y) * rebound_coefficient * 1.2
    return position, velocity


def update_blue_ball_ai():
    global blue_ball_velocity
    target_direction = (yellow_ball_pos - blue_ball_pos).normalize()
    blue_ball_velocity += target_direction * blue_ball_acceleration

    if blue_ball_velocity.magnitude() > blue_ball_max_speed:
        blue_ball_velocity = blue_ball_velocity.normalize() * blue_ball_max_speed
    blue_ball_velocity *= 0.99


def update_yellow_ball_ai():
    global yellow_ball_velocity
    escape_direction = (yellow_ball_pos - player.center).normalize() + (yellow_ball_pos - blue_ball_pos).normalize()
    escape_direction = escape_direction.normalize()

    if yellow_ball_pos.x < 150 or yellow_ball_pos.x > SCREEN_WIDTH - 150:
        escape_direction.y += 0.8 * (-1 if yellow_ball_pos.y < SCREEN_HEIGHT / 2 else 1)
    if yellow_ball_pos.y < 150 or yellow_ball_pos.y > SCREEN_HEIGHT - 150:
        escape_direction.x += 0.8 * (-1 if yellow_ball_pos.x < SCREEN_WIDTH / 2 else 1)

    yellow_ball_velocity += escape_direction * 0.035
    if yellow_ball_velocity.magnitude() > 35:
        yellow_ball_velocity = yellow_ball_velocity.normalize() * 35


def draw_interface():
    if game_running:
        remaining_time = game_duration - (pygame.time.get_ticks() - start_time) // 1000
        score_text = font.render(f"分数: {score:.1f}", True, "white")
        time_text = font.render(f"剩余时间: {remaining_time}秒", True, "white")
        screen.blit(score_text, (10, 10))
        screen.blit(time_text, (10, 50))
    else:
        screen.fill("black")
        final_score_text = larger_font.render(f"最终得分: {score:.1f}", True, "yellow")
        prompt_text = font.render("按回车键重新开始", True, "white")
        screen.blit(
            final_score_text,
            (
                SCREEN_WIDTH // 2 - final_score_text.get_width() // 2,
                SCREEN_HEIGHT // 2 - 50,
            ),
        )
        screen.blit(
            prompt_text,
            (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50),
        )


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
            elif event.key == pygame.K_RETURN and not game_running:
                reset_game()

    if game_running:
        # Update key timers
        keys = pygame.key.get_pressed()
        for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
            key_timer[key] = key_timer[key] + 1 if keys[key] else 0

        # Player movement
        y_speed = player_base_speed
        x_speed = player_base_speed

        if keys[pygame.K_UP] and key_timer[pygame.K_UP] > acceleration_threshold:
            y_speed *= acceleration_factor
        if keys[pygame.K_DOWN] and key_timer[pygame.K_DOWN] > acceleration_threshold:
            y_speed *= acceleration_factor

        if keys[pygame.K_LEFT] and key_timer[pygame.K_LEFT] > acceleration_threshold:
            x_speed *= acceleration_factor
        if keys[pygame.K_RIGHT] and key_timer[pygame.K_RIGHT] > acceleration_threshold:
            x_speed *= acceleration_factor

        # Use temporary variables to store player coordinates to avoid repeated calculations
        new_y_position = player.y
        new_x_position = player.x

        # Calculate new y coordinate, limit within screen range
        new_y_position -= keys[pygame.K_UP] * y_speed
        new_y_position = max(0, min(SCREEN_HEIGHT - PLAYER_SIZE, new_y_position))

        # Calculate new x coordinate, limit within screen range
        new_x_position -= keys[pygame.K_LEFT] * x_speed
        new_x_position = max(0, min(SCREEN_WIDTH - PLAYER_SIZE, new_x_position))

        # Update player position
        player.y = new_y_position
        player.x = new_x_position

        # Update blue ball
        update_blue_ball_ai()
        blue_ball_pos += blue_ball_velocity
        blue_ball_pos, blue_ball_velocity = handle_boundary(blue_ball_pos, blue_ball_velocity, ball_radius)

        # Update yellow ball
        update_yellow_ball_ai()
        yellow_ball_pos += yellow_ball_velocity
        yellow_ball_pos, yellow_ball_velocity = handle_boundary(yellow_ball_pos, yellow_ball_velocity, ball_radius)

        # Collision handling
        if ball_collision_detection(blue_ball_pos, yellow_ball_pos, ball_radius):
            try:
                collision_direction = (yellow_ball_pos - blue_ball_pos).normalize()
            except ZeroDivisionError:
                collision_direction = Vector2(1, 0)  # Default direction

            blue_ball_velocity = -collision_direction * collision_force * 0.7
            yellow_ball_velocity = collision_direction * collision_force * 1.4
            score += SCORE_SMALL

        if detect_collision(player, yellow_ball_pos, ball_radius):
            try:
                direction = (yellow_ball_pos - player.center).normalize()
            except ZeroDivisionError:
                direction = Vector2(1, 0)  # Default direction

            yellow_ball_velocity = direction * collision_force * 1.2
            score += SCORE_LARGE

        if detect_collision(player, blue_ball_pos, ball_radius):
            try:
                direction = (blue_ball_pos - player.center).normalize()
            except ZeroDivisionError:
                direction = Vector2(1, 0)  # Default direction

            blue_ball_velocity = direction * collision_force * 0.8

        # Check time
        if (pygame.time.get_ticks() - start_time) // 1000 >= game_duration:
            game_running = False

    # Render
    screen.fill("black")
    if game_running:
        pygame.draw.rect(screen, "red", player)
        pygame.draw.circle(screen, "blue", blue_ball_pos, ball_radius)
        pygame.draw.circle(screen, "yellow", yellow_ball_pos, ball_radius)
    draw_interface()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# ==========================================================================

a = 100
b = 200
print(a, b, '装逼，我让你飞起来')  # 这是一个简单的代码
c = 50
d = 100
e = 200
print(c * d / e)
print(c + d)
print("你好啊，晚上好！")
# ================================================
print('b')
print(chr(98))
print('c')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
print(ord('你'), ord('好'))
print(chr(20320), chr(22909))
# ================================================
flag = False  # 标记，我是错的
name = 'liunx'  # 曾经的小企鹅
if name == 'liunx':  # 判断变量name的值是否等于'liunx'
    flag = True  # 改成真的
    print('你好啊，新同学！')  # 并输出欢迎信息
else:
    print(name)  # 条件不成立时输出变量名称
# ===================================================
num = 0  # 数字为0
if num == 3:  # 判断Num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num == 0:
    print('nimalege')
elif num < 0:  # 值小于零时输出
    print('error')
else:
    print('roadman')  # 条件不成立时输出
# ===============================================
can = 9
if 0 <= can <= 10:  # 判断值是否在0~10之间
    print('你好，你好？你好！')
# 输出结果：我不好

zhe = 10
if 0 > zhe > 10:  # 判断值是否在小于0或大于10（挺苛刻的）
    print('我上早八')
else:
    print('宝了个贝的，这是给我干那来了，这还是国内吗？')
# 输出结果：孩子，这并不好笑

cao = 8
# 判断值是否在0~5或者10~15之间
if (0 <= cao <= 5) or (10 <= cao <= 15):
    print('我测你温码')
else:
    print('我是丁真，这是我的好朋友芝士雪豹。')
# 输出结果：嗷呜~ 雪豹别叫!
# ==============================================
var = 100
if var == 100:
    print("太好啦，是烧鸡，我们没救了！"
          "\n心还没有悬着就去世了！")
guzhenren = '大专巅峰'
if guzhenren == '大专巅峰':
    print("“你到底干了什么，你不跟我们干，我们以后怎么赚大钱”室友跺着脚恶狠狠地瞪着他。")
    print("他淡然一笑“很简单，我进厂不就是了”说完，他的气息不再掩饰，显露而出，大专巅峰！！\n一瞬间，流水线再次一寂。")
    time.sleep(1)
    print("我乃大专巅峰！何人敢叼我，何人能叼我！他口中低吟道：")
    print("电子厂中寒风吹，流水线上大神归")
    time.sleep(0.5)
    print("一号工位黑奴泪，褪去校服人向北")
    time.sleep(0.5)
    print("无休倒班万人退，三千工资空落泪")
    time.sleep(0.5)
    print("宿命天成当厂妹，本科悔而我不悔!")
    time.sleep(0.5)
    print("早岁已知挣钱艰，仍许资本荡人间")
    time.sleep(0.5)
    print("十年苦读身如絮，无尘车间客独行")
    time.sleep(0.5)
    print("千磨万击手铸铁，殚精竭虑打工件")
    time.sleep(0.5)
    print("今朝人向工位处，打件打人还打天")
    time.sleep(0.5)
    print(
        "从今以后，他就彻底从一位学生变成一位打工人，可以堂堂正正的打螺丝，造福车间了，工友们的历史，资本家们的历史不得不记载他的名字，至此他和数百位工友并肩，宛若大日光照千古，其余同学无论多么豪杰英雄，皆为繁星。")
collegeStudents = '大专生发言'
if collegeStudents == '大专生发言':
    print('不过是些许风霜罢了')
    print('面对凶险万分的流水线，不退反进，仰天大喝：件来！')
    print('今朝剑指叠云处，炼蛊炼人还炼天')
# ================================================
age = input('打出你的年龄: ')  # 输入你的年龄
print(age)  # 输出你的输入
# ================================================
x = 10
y = 5
s = x * y
print(s)  # 50
# ================================================
result = '我' + '和' + '你'
print(result)  # 输出“我和你”
# ================================================
a, b, c = 1, 2, 'jojo'  # 我居然忘记了还有这个
print(a, b, c)
# ================================================
stir = '你好啊，外邦的旅客！'  # 列表啦！
print(stir)
print(stir[0])  # 索引
print(stir[1])
print(stir[2:5])  # 切片
print(stir[2:])
print(stir * 2)
print(stir + "end")
print(stir[:7])
# ===============================================
lisut = ['What can I say?', 786, 2.23, 'jojo', 70.2]
tinylisut = [123, 'jojo']
print(lisut)
print(lisut[0])
print(lisut[1:3])
print(lisut[2:])
print(tinylisut * 2)
print(lisut + tinylisut)
# ===============================================
dicat = {'我来助你！': "广智救我！", '出门撞大运': "新年快乐！"}

tinydicat = {'米饭仙人': '风灵月影', '刚满18岁': 114514, '我这一生如履薄冰': '菜就多练'}

print(dicat['我来助你！'])  # 字典中的键值对
print(dicat['出门撞大运'])
print(tinydicat)  # 字典中的键值对
print(tinydicat.keys())  # 字典的键
print(tinydicat.values())  # 字典的值
print(tinydicat.items())  # 字典的键值对
print(dicat.items())  # 字典的键值对
print(dicat.keys())  # 字典的键
print(dicat.values())  # 字典的值
# ===============================================
a = 21
b = 10
c = 0

if a == b:
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if a != b:
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if a != b:
    print("3 - a 不等于 b")
else:
    print("3 - a 等于 b")

if a < b:
    print("4 - a 小于 b")
else:
    print("4 - a 大于等于 b")

if a > b:
    print("5 - a 大于 b")
else:
    print("5 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print("6 - a 小于等于 b")
else:
    print("6 - a 大于  b")

if b >= a:
    print("7 - b 大于等于 a")
else:
    print("7 - b 小于 a")
# ======================================
a = '就凭你也配直视我！'  # 神
b = '把头低下！'  # 精
lisut = ['诶呀', '真的是你呀', '哈哈', '嗐呦', 'baby']  # 练习生

if a in lisut:  # 如果，“神”在“练习生”里。就告诉你，勇敢去做，否则，没有不可能
    print("勇敢去做")  # 对
else:  # 不
    print("没有不可能")  # 对

if b not in lisut:  # 如果“神精”在“练习生”里，就偷懒
    print("2 - 变量 b 不在给定的列表中 list 中")  # 懒
else:  # 否则
    print("2 - 变量 b 在给定的列表中 list 中")  # 偷

# 修改变量 a 的值
a = '真的是你呀'  # 练习时长两年半
if a in lisut:  # 如果你有两年半的练习
    print("3 - 变量 a 在给定的列表中 list 中")  # 你就练习了两年半
else:  # 杂鱼
    print("3 - 变量 a 不在给定的列表中 list 中")  # 错过就是失去，你明白了吗。
# ===========================================================================
a = 20  # 变量为20
b = 10  # 10
c = 15  # 15
d = 5

e = (a + b) * c / d  # ( 20 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)  # 输出上面的式子

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)  # 费手

e = (a + b) * (c / d)  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)  # 一对对照组

e = a + (b * c) / d  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)  # 看，电灯泡
# =======================================================
count = 0  # 设定函数值为0
while count < 9:  # 在当函数值小于9的条件下循环输出以下内容
    print('The count is:', count)  # 输出，包含下一个变量
    count = count + 1  # 每一次循环都加1
# 改循环会将count一直加一，并且输出该数，直到count》=9，循环结束
print("On my god!")  # 天才
var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去（死循环）
    num = input("随便 :")  # 随便写一个，回车
    print("写了个寂寞: ", num)  # 输出你刚刚写下的东西
    if num == '1314':  # 当你输入一生一世时，循环终止
        break
print("拜拜!")  # 友好的再见
count = 0
while count < 5:
    print(count, " 小于5")
    count = count + 1
else:
    print(count, "不小于5")
# 模块开头已给出
keep_running = True
start_time = time.time()

while keep_running:
    print('给定的标志确实为真！')
    # 5 秒后终止循环
    if time.time() - start_time > 5:
        keep_running = False
    time.sleep(0.1)  # 降低 CPU 占用
# ===================================================
for letter in '一个字，绝':  # 第一个实例，一个字一个字地输出
    print("看看看看: %s" % letter)

fruits = ['唱', '跳', 'rap', '篮球']
for fruit in fruits:  # 第二个实例，一个元素一个元素地输出
    print('真的是你呀，哈哈！: %s' % fruit)

fruits = ['鸡', '你', '太美']
for index in range(len(fruits)):
    print('真的是你呀！哈哈 ： %s' % fruits[index])
# ====================================================
for num in range(10, 20):  # 迭代 10 到 20 (不包含) 之间的数字,简单来说就是10~19
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)

# ===============================================
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j += 1
    if j > i / j:
        print(i, " 是素数")
    i += 1
# ==============================================
apple = 'eat'  # 吃苹果
kill = 'eat'  # 修正了这里，将 kill 的值改为 'eat'
I1 = 'you'
kiss = 'you'

# 检查条件是否满足
if apple == kill and I1 == kiss:
    print(
        '''一袋米要抗几楼（感受痛苦吧），
一袋米要抗二楼（思考痛苦吧），
一袋米要给多了（接受痛苦吧），
一袋米我洗嘞（理解痛苦吧），
一袋米我洗了那么多泥（不了解痛楚的人），
和那堆黑瓦，瓦坷垃（是无法了解真正的和平的）！
颗颗有泥（从现在开始），
谁给你一袋米呦（让世界感受痛苦），
行了添水 / 辛辣天森 / 心累天塞（神罗天征）！'''
    )
elif apple == kill and I1 != kiss:
    print('一袋米引发的战争')
'''试了三次啊，三次，终于成功了'''
# ========================================================
a = input("第一个数字：")
b = input("第二个数字：")
# print(type(a))  # 查看变量类型
a = int(a)  # 将变量a 转换为整数类型
b = int(b)
# print(type(a))
print(a + b)
# ================================
money = int(input("交出你的money，哈哈哈: "))  # 要钱
if money >= 500:
    print("太好啦，是钱，我们有救了！")  # 太好了，是甲方
else:
    print("太好了，让我们进入米奇妙妙屋。")  # （勉强的笑容）
if money >= 1000:
    if 1000 < money < 5000:
        print('加油加油！')  # 厉害了我的哥
    elif money == 1000:
        print('有所懈怠了呀。')  # 基本满足
    if money == 1000:
        print('刚刚好，是不是故意的？')  # 黑暗森林，有着猜疑链
if 500 <= money <= 1000:
    if money == 500:
        print('回家吧，你也不希望在外面出丑吧？')  # 可以吃饭
    if money == 1000:
        print('不是故意的，就是有意的！')  # 自问自答
    if 500 < money < 1000:
        print('你的想法真是让人捉摸不透啊！')  # 呀呀呀呀
    else:
        print('嘿，你瞅啥呢，我是你蝶！')  # 哎呀呀
# ================================================
a = int(input("来来来（数字，不要提前回车）："))
b = 0
while b <= 100:  # 用while循环100次，哈哈哈
    print(a)
    b += 1
    a += b
    print(b)
    a -= b  # 还是徒劳吗？
    # break 用break直接结束循环
# ====================================时间戳的运用示例
# 获取当前时间戳（秒级时间戳）
timestamp = time.time()
print("当前时间戳（秒）:", timestamp)

# 获取当前时间戳（毫秒级时间戳）
timestamp_ms = int(round(time.time() * 1000))
print("当前时间戳（毫秒）:", timestamp_ms)

# 将秒级时间戳转换为日期时间
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)
print("从时间戳转换为日期时间:", dt)

# 将毫秒级时间戳转换为日期时间

timestamp_ms = 1672531200000  # 示例毫秒级时间戳
dt_ms = datetime.fromtimestamp(timestamp_ms / 1000)
# 使用更精确的毫秒转换方法
milliseconds = timestamp_ms % 1000
dt_ms_precise = datetime.fromtimestamp(timestamp_ms // 1000) + timedelta(milliseconds=milliseconds)
print("从毫秒级时间戳转换为日期时间:", dt_ms_precise)

# 将日期时间转换为秒级时间戳
dt = datetime.now()
timestamp = dt.timestamp()
print("从日期时间转换为时间戳（秒）:", timestamp)

# 将日期时间转换为毫秒级时间戳
timestamp_ms = int(dt.timestamp() * 1000)
print("从日期时间转换为时间戳（毫秒）:", timestamp_ms)

# 获取当前时间戳并格式化为日期时间字符串
timestamp = time.time()
formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
print("格式化的时间:", formatted_time)

# 计算两个时间戳之间的时间差
try:
    timestamp1 = time.time()
    time.sleep(2)  # 模拟等待2秒
    timestamp2 = time.time()

    # 计算时间差（秒）
    if timestamp2 >= timestamp1:
        time_diff = timestamp2 - timestamp1
        print("时间差（秒）:", time_diff)
    else:
        raise ValueError("时间戳2必须大于等于时间戳1")
except Exception as e:
    print(f"时间计算错误: {e}")

# 创建一个日期时间对象
dt = datetime.now()
print("当前日期时间:", dt)

# 日期时间加减操作前增加边界检查
if isinstance(dt, datetime):
    # 添加时间
    new_dt = dt + timedelta(days=1, hours=2, minutes=30)
    print("添加时间后:", new_dt)

    # 减去时间
    old_dt = dt - timedelta(days=1)
    print("减去时间后:", old_dt)
else:
    print("错误：无效的日期时间对象")

# 定义两个日期时间
start_time = datetime(2024, 1, 1)
end_time = datetime(2024, 1, 15)

# 两个日期之间的时间戳差值计算时增加有效性检查
if end_time > start_time:
    time_diff = (end_time - start_time).total_seconds()
    print("两个日期之间的时间戳差（秒）:", time_diff)
else:
    print("错误：结束时间必须大于开始时间")
# ========================================================时间控制循环示例（好玩）
# 使用 time.time() 来控制循环时间

# 设置循环的最大运行时间（秒）
max_duration = 5  # 例如，让循环运行 5 秒

# 记录循环开始的时间
start_time = time.time()

while True:
    # 检查是否超过时间限制
    if time.time() - start_time > max_duration:
        print("循环运行时间已超过限制，停止循环。")
        break

    # 循环内的代码
    print("我是time.time()")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

# 使用 datetime.timedelta 来控制循环时间

# 设置循环的最大运行时间（秒）
max_duration = 5  # 例如，让循环运行 5 秒

# 记录循环开始的时间
start_time = datetime.now()

while True:
    # 检查是否超过时间限制
    if (datetime.now() - start_time).total_seconds() > max_duration:
        print("循环运行时间已超过限制，停止循环。")
        break

    # 循环内的代码
    print("我是datetime.timedelta")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

'''# 使用 signal 模块（仅限 Unix 系统）
import signal
import time

# 定义一个标志变量，用于控制循环
stop_loop = False

# 定义信号处理函数
def handle_timeout(signum, frame):
    global stop_loop
    print("时间限制已到，停止循环。")
    stop_loop = True

# 设置信号处理
signal.signal(signal.SIGALRM, handle_timeout)
signal.alarm(5)  # 设置 5 秒后发送 SIGALRM 信号

try:
    while not stop_loop:
        print("循环正在运行...")
        time.sleep(1)  # 模拟每次循环耗时 1 秒
finally:
    signal.alarm(0)  # 取消定时信号'''

# 使用多线程
# 定义一个标志变量，用于控制循环
stop_loop = False


def stop_after_timeout(duration):
    global stop_loop
    time.sleep(duration)
    stop_loop = True
    print("时间限制已到，停止循环。")


# 设置时间限制
timeout = 5  # 例如，让循环运行 5 秒

# 启动一个线程来控制时间
thread = threading.Thread(target=stop_after_timeout, args=(timeout,))
thread.start()

# 主循环
while not stop_loop:
    print("注意，我是多线程")
    time.sleep(1)  # 模拟每次循环耗时 1 秒

thread.join()  # 等待线程结束


# 使用 asyncio（异步方式）


async def main():
    # 设置循环的最大运行时间（秒）
    max_duration = 5  # 例如，让循环运行 5 秒

    # 记录循环开始的时间
    start_time = asyncio.get_event_loop().time()

    while True:
        # 检查是否超过时间限制
        if asyncio.get_event_loop().time() - start_time > max_duration:
            print("循环运行时间已超过限制，停止循环。")
            break

        # 循环内的代码
        print("我是asyncio")
        await asyncio.sleep(1)  # 模拟每次循环耗时 1 秒


# 运行异步主函数
asyncio.run(main())
# ==========================================================
s = "这是真的啊，你不会忘了吧？"
for i in s:
    print("这一次，请确定:", i)

for i in range(10):  # 从0数到10，但不包含10
    print(i)

for i in range(3, 10):  # 3~9
    print(i)

i = 1
while i <= 10:  # 成立
    print(i)
    i += 2  # 由i = i + 2简化而来

for i in range(1, 10, 2):  # 1~9,跳过2
    print(i)  # 就是只输出1 3 5 7 9

x = 10
if x > 5:
    pass  # 跳过，下次想好了再补充
print("吹牛逼呢，见过吗，这叫俄罗斯大贝塔，你就只能看着我骑")
# ============================================================
# 使用标志变量 + 时间戳（无需多线程）

start_time = time.time()
timeout = 5  # 5秒后停止

while True:
    # 循环内执行你的操作
    print("循环运行中...")
    time.sleep(1)  # 模拟操作耗时

    # 检查是否超时
    if time.time() - start_time > timeout:  # 用现在比较过去，你还会犹豫吗？
        print("已超时，停止循环")
        break

# 使用多线程 + 定时器（精确控制）


# 控制循环运行的标志
running = True


def stop_loop():
    global running
    running = False
    print("\n5秒时间到，停止循环")


# 设置5秒后执行停止函数
timer = threading.Timer(5.0, stop_loop)
timer.start()

# 主循环
while running:
    print("循环运行中...", end='\r')
    time.sleep(0.1)  # 短暂休眠避免过度占用CPU

print("循环已结束")
# ===========================================================
# int:整数，可以进行整数之间的加减乘除，以及比较大小
# 比如：
"""a = 10
b = 15
print(a + b)
print(a - b)
print(a * b)
print(a / b)
if a < b:
    print('a < b')
if a > b:
    print('a > b')
if a == b:
    print('a == b')
if a >= b:
    print('a >= b')
if a <= b:
    print('a <= b')

# float:小数，浮点数
# 比如:
a = 10.57
print(a)
# 但是，有一个无限小数点
# 比如：
print(10 / 3)  # 它的输出的最后一位存在误差，说明关于无穷，计算机也是只能给出不准确的数
# 还有，小数的数据范围是无限的，而整数会在某一个特定区间内是可以清楚表示的
# 就像你与你命中注定的人的距离，处于小数时，距离是可以无限近和无限远的。但是，处于整数时，在一瞬间，你们两个的关系就明确了
# 计算机是一款二进制产品，语言基础就：0,1，人家本来就难，不要强迫别人，所以，计算机在表示一个小数时是会有误差的
# bool : 用来做条件判断的，取值范围只有 True 和 False ，基础数据类型之间的转换
a = "10"  # 字符串
print(type(a))
b = int(b)
print(type(b))
a = 0        # 在python中，所有的非零的数字都是 Ture，零是 False
b = bool(a)
print(type(b))
print(b)

while a:     # 无限循环,恒为真
    print("你好吗？我吃柠檬！")

s = ""    # 在python中，所有的非空字符串都是 Ture，空字符串是 False
print(bool(s))"""

# # 综上，在python中，表示空的东西都是False，不空的东西都是True
# lst = [0]
# print(bool(lst))


# while 1:
#     content = input("请输入你想要的内容：")
#     if content:
#         print("你要发给某人的内容：", content)
#     else:
#         break

# ===============================================================
# 蛊界的那些事

# 定义对话内容的字典
dialogues = {
    "blood_skull_gu": {
        "condition": "众人所望",
        "content": '''古月族长：
方源，你不要再妇人之仁了。
快对我们使用血颅蛊，
再晚就来不及了，
你难道要看着我们古月一族，
彻底消失吗？'''
    },
    "fang_yuan_crying": {
        "condition": "哭泣",
        "content": '''方源：
不，族长爷爷，
我不能这样，
我不能这样！
我要陪你们一起战斗，我们还有希望的！'''
    },
    "combined_dialogue": {
        "condition": ("众人所望", "哭泣"),
        "content": '''古月族长：
没有机会了。
吐血；
古月方源，
我以古月一族之长的身份命令你
咳血*2；
立刻使用血颅蛊，活下去...重振我古月一族
否则，你再也不是我古月一族之人！

方源爆发：
族长爷爷，族人们，
你们放心，我一定会重振古月一族的辉煌，
我会为你们报仇，还要从仙鹤门手中救出弟弟
仙鹤门，我古月方源对天发誓，有朝一日，定让你们鸡犬不留...'''
    },
    "gu_zhen_ren": {
        "condition": "方源诵诗",
        "content": '''落魄谷中寒风吹，春秋蝉鸣少年归。
荡魂深处石人泪，定仙游走魔向北。
逆流河上万仙退，爱情不敌坚持泪。
宿命中成命中败，仙尊悔，而我不悔！'''
    },
    "fang_yuan_history": {
        "condition": "历史，如果有用还要我有什么用！！！",
        "content": [
            ('10岁', '青梅竹马，献祭自己，为主角增长修为 三转'),
            ('15岁', '全族为了保住家族火种，强行为主角提升资质，甲等'),
            ('18岁', '为保护八十八角真阳楼，无奈放弃前途成仙'),
            ('20岁', '被尊者作为蛊虫实验品，天妒'),
            ('25岁', '被双尊合力打杀，弥留之际，光阴长河中传来一句诛心之言')
        ],
        "conclusion": "你... 可曾有一丝后悔\n少年微笑 不过是些许风霜罢了 维护他人，无悔"
    },
    "bai_ning_bing": {
        "content": '''为什么都说 白凝冰 实际上才是蛊真人笔下的第一女主呢？
因为她说：
这个蛊界好不公平
我陪你从古月山寨一直走到了三王山，
见证你以蛊师之身，
练出了六转仙蛊，
可是几年后出现的星宿仙尊，
却轻易地夺走了那个最好的你，
未来会更好的你
爱情，真的要这么毫无道理吗？
对于蛊界，你是冷酷残忍的炼天魔尊，
但是对我来说，你就是那个只为造福世界，恢复五域和谐的大爱仙尊啊！

4月23，和方源一起吃冰淇淋，甜甜的很好吃，方源还帮我擦嘴
4月24，和方源去商量山，世界最暖和的地方在商家的演武场
4月25，和方源去三王山，有人在那里炼仙蛊，不知道会是什么呢
4月26，和方源去天庭，星宿仙尊很可怕，但是有方源在，所以不可怕
方源最好了，冰冰只爱方源'''
    },
    "girl_toy_scene": {
        "content": '''女童：哎呀，我的玩具
一个女童叫着，在人群中追逐着陀螺，陀螺恰好滚到了方源的脚下，女童也撞到了方源的腿上，跌倒在地
女童的父亲：诶呀，女儿你都干了什么，冲撞了估摸师大人我们拿什么活命啊？
女童的父亲连忙赶到，看到方源的服饰，脸色吓得惨白如纸，急忙拉起女童，扑通就跪了下来
女童的父亲：不要哭，闯祸精！
父亲又惊又怒又怕，一个巴掌甩了过去，却被方源伸手抓住
方源：只是一点小事，无需挂怀
方源淡淡一笑，伸手摸向女童的小脑袋，轻声安慰道：“没事的，不用害怕。”
女童也在此刻抬起头颅，方源瞳孔猛地一缩，察觉到了不对劲。此时，女童缓缓起身，旋即用稚嫩的语气轻笑一声道：
“嘿嘿，方源大哥哥，很简单，我成尊不就是了”
说完，她的气息不再掩饰，显露而出，九转修为。方源大惊失色，春秋蝉也被这气息死死压住，动弹不得
女童一身单薄素衣随风飘扬，清了清嗓子，悠悠吟道：
“早岁已知人贪玩，仍许陀螺碰方源。
飞转缥缈身如燕，翩翩起舞姿无限。
万念童心未曾泯，生死有命只问天。
今朝陀出风云起，转蛊转人还转天！”'''
    }
}


# 封装打印函数
def print_with_delay(content, delay=1):
    try:
        print(content)
        time.sleep(delay)
    except KeyboardInterrupt:
        print("\n程序被用户中断")


# 主逻辑
if dialogues["blood_skull_gu"]["condition"] == "众人所望":
    print_with_delay(dialogues["blood_skull_gu"]["content"])

if dialogues["fang_yuan_crying"]["condition"] == "哭泣":
    print_with_delay(dialogues["fang_yuan_crying"]["content"])

if (dialogues["blood_skull_gu"]["condition"], dialogues["fang_yuan_crying"]["condition"]) == \
        dialogues["combined_dialogue"]["condition"]:
    print_with_delay(dialogues["combined_dialogue"]["content"], delay=1)

if dialogues["gu_zhen_ren"]["condition"] == "方源诵诗":
    print_with_delay(dialogues["gu_zhen_ren"]["content"])

if dialogues["fang_yuan_history"]["condition"] == "历史，如果有用还要我有什么用！！！":
    for age, event in dialogues["fang_yuan_history"]["content"]:
        print(f"{age} {event}")
    print(dialogues["fang_yuan_history"]["conclusion"])
    print_with_delay("顷刻间，尊者，成")

print_with_delay(dialogues["bai_ning_bing"]["content"])
print_with_delay(dialogues["girl_toy_scene"]["content"])
# ==============================================================

# 设置屏幕
screen = Screen()  # screen是变量
screen.setup(600, 400)  # 设置屏幕大小
screen.bgcolor("red")  # 设置背景颜色

# 创建画笔
pen = Turtle()  # pen是变量
pen.speed(10)  # 设置画笔速度为10
pen.penup()  # 设置画笔抬起


# 绘制大五角星
def draw_star(x, y, size):
    # 定义函数draw_star,def是声明后方的代码是函数
    pen.goto(x, y)  # 设置画笔位置为x,y
    pen.pendown()  # 设置画笔落下
    pen.color("yellow")  # 设置画笔颜色为黄色
    pen.begin_fill()  # 开始填充
    for _ in range(5):  # 循环五次
        pen.forward(size)  # 画笔向前移动size
        pen.right(144)  # 设置画笔向右旋转144度
    pen.end_fill()  # 结束填充
    pen.penup()  # 设置画笔抬起


# 绘制大五角星
draw_star(-200, 100, 100)  # 调用函数draw_star


# 绘制四个小五角星
def draw_small_star(x, y, size, angle):
    # 定义函数draw_small_star
    pen.goto(x, y)  # 设置画笔位置为x,y
    pen.setheading(angle)  # 设置画笔朝向angle度
    pen.pendown()  # 设置画笔落下
    pen.color("yellow")  # 设置画笔颜色为黄色
    pen.begin_fill()  # 开始填充
    for _ in range(5):  # 循环五次
        pen.forward(size)  # 设置画笔向前移动size
        pen.right(144)  # 设置画笔向右旋转144度
    pen.end_fill()  # 结束填充
    pen.penup()  # 设置画笔抬起


# 绘制四个小五角星
draw_small_star(-100, 160, 30, 30)  # 调用函数draw_small_star
draw_small_star(-60, 120, 30, 0)  # 调用函数draw_small_star
draw_small_star(-60, 60, 30, -30)  # 调用函数draw_small_star
draw_small_star(-100, 20, 30, -60)  # 调用函数draw_small_star

# 隐藏画笔
pen.hideturtle()

# 结束
done()  # 阻塞程序并保持窗口打开，直到用户手动关闭
# mainloop()
# ===============================================================
'''speed(0)    # 设置最快速度
tracer(0)   # 关闭自动刷新
# ==================================
# 四个圆
a = 1
while a <= 4:
    circle(100)
    right(90)
    a += 1

update()     # 最终刷新画面
time.sleep(5)    # 保持窗口显示（可选）

# circle(100)
# left(180)
# ===================================
# 球
for i in range(100):
    circle(100)
    right(91)
done()
# ===================================
# 四方相回
for i in range(100):
    circle(i)
    right(91)
done()
# ==================================
# 彩色的圆
for i in range(100):
    circle(i)
    right(91)
    color("red")
    color("blue")
    color("green")
    color("yellow")
    color("pink")
    color("purple")
    color("orange")
    color("black")
    color("white")
done()
# ==================================
# 不好看

# 颜色配置优化方案
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
speed(0)  # 设置最快绘制速度

for i in range(100):
      # 通过取余实现颜色循环
    color(colors[i % len(colors)])
    circle(i)
    right(91)

done()
# ==================================
# 好看吗？

# 方式1：使用随机RGB颜色（更丰富的色彩）
colormode(255)  # 必须设置颜色模式
speed(0)

for i in range(100):
      # 生成随机RGB颜色
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color((r, g, b))

    circle(i)
    right(91)

done()
# ==================================
# 蓝球
color('blue')
for i in range(100):
    circle(i)
    right(78)
# ==================================
# 奥运五环
pensize(9)

color('black')
circle(75)

penup()
goto(-180,0)
pendown()
color('blue')
circle(75)

penup()
goto(180,0)
pendown()
color('red')
circle(75)

penup()
goto(90,-75)
pendown()
color('green')
circle(75)

penup()
goto(-90,-75)
pendown()
color('yellow')
circle(75)

color('black')
penup()
goto(-100,180)
pendown()
write('北京 2020',font=('Haiti',32))
hideturtle()
# ==================================
# 美国盾牌
penup()
goto(0,-200)
pendown()
color('red')
begin_fill()
circle(200)
end_fill()

penup()
goto(0,-150)
pendown()
color('white')
begin_fill()
circle(150)
end_fill()

penup()
goto(0,-100)
pendown()
color('red')
begin_fill()
circle(100)
end_fill()

penup()
goto(0,-50)
pendown()
color('blue')
begin_fill()
circle(50)
end_fill()

penup()
goto(-40,10)
pendown()

color('white')

begin_fill()

for i in range(5):
    forward(80)
    right(144)

end_fill()

hideturtle()
# =================================
# 彩球飘飘

# 随机数

colormode(255)
speed(0)

for i in range(20):
    red = random.randint(0,255)  # 在这里调颜色
    green = red = random.randint(0,255)
    blue = red = random.randint(0,255)

    x = random.randint(-220,220)
    y = random.randint(-100,220)

    penup()
    goto(x,y)
    pendown()

    color(red,green,blue)

    begin_fill()
    circle(30)
    end_fill()

    right(90)
    forward(30)
    left(90)
done()
# RGB red green blue
# ==================================
# 繁星满天
color('black')

speed(0)
colormode(255)

pensize(250)
for i in range(10):
    goto(-500,300-i*100)
    color(i*20,i*20,i*20)
    forward(1000)

for x in range(8):
    if x%2==0:
        left(30)
    else:
        right(120)
    forward(50)
for i in range(20):
    x = random.randint(-400,400)
    y = random.randint(-100,350)
    e = random.randint(1, 15)
    def drawStar():
        begin_fill()
        for i in range(4):
            forward(e)
            left(30)
            forward(e)
            right(120)
        end_fill()

    pensize(5)
    penup()
    goto(x, y)
    # goto(150,150)
    pendown()
    red = random.randint(180,255)
    green = random.randint(180,255)
    blue = 0
    color(red, green, blue)
    drawStar()'''
# ===================================
mc = int(input('请输入排名：'))  # 输入排名进行加分
lst = [7, 5, 4, 3, 2, 1]
if 1 <= mc <= 6:
    df = lst[mc - 1]
    print(f'加{df}分')  # 效果相同，更直观简洁
else:
    print('输入错误，不在1~6内！')
# ====================================
# 小游戏，随机数模拟色子
money = 10000000
number_of_times = 0
game_player = 0
dealer = 0
while True:
    while money > 0:
        number_of_times += 1
        print(f'第{number_of_times}局\n你的总资产为: {money}元')
        # time.sleep(2)
        # 下注金额必须大于0且小于等于玩家的总资产
        while True:
            # debt = int(input('请下注: '))
            debt = random.randint(0, money)
            print(f'你下注了{debt}元')
            # time.sleep(2)
            if 0 < debt <= money:
                break
        # 用两个1到6均匀分布的随机数相加模拟摇两颗色子得到的点数
        first_point = random.randrange(1, 7) + random.randrange(1, 7)
        print(f'\n玩家摇出了{first_point}点')
        if first_point == 7 or first_point == 11:
            print('玩家胜!\n')
            money += debt
            game_player += 1
        elif first_point == 2 or first_point == 3 or first_point == 12:
            print('庄家胜!\n')
            money -= debt
            dealer += 1
        else:
            # 如果第一次摇色子没有分出胜负，玩家需要重新摇色子
            while True:
                current_point = random.randrange(1, 7) + random.randrange(1, 7)
                print(f'玩家摇出了{current_point}点')
                if current_point == 7:
                    print('庄家胜!\n')
                    money -= debt
                    dealer += 1
                    break
                elif current_point == first_point:
                    print('玩家胜!\n')
                    money += debt
                    game_player += 1
                    break
    print(f'你破产了, 游戏结束!\n已自动进行了{number_of_times}局游戏\n你胜利了{game_player}局, 失败了{dealer}局')
    anan = input('是否继续游戏(an): ')
    if anan == 'an':
        money = 10000000
        number_of_times = 0
        game_player = 0
        dealer = 0
    else:
        break
# ====================================
counters = [0] * 6
# 模拟掷色子记录每种点数出现的次数
for _ in range(6000):
    face = random.randrange(1, 7)
    counters[face - 1] += 1
# 输出每种点数出现的次数
for face in range(1, 7):
    print(f'{face}点出现了{counters[face - 1]}次')
# ====================================
# 1. 字符串格式化
# 我叫xxx，我住在xxx，我今年xxx岁，我的爱好是xxx
# name = input("请输入你的名字：")
# address = input("请输入你的地址：")
# age = int(input("请输入你的年龄："))
# hobby = input("请输入你的爱好：")

# %s 字符串占位（也可以表示整数和小数，也可以说是万能的）
# %d 整数占位
# %f 浮点数占位（简单来说就是小数占位）
# s = "我叫%s，我住在%s，我今年%d岁，我的爱好是%s" % (name, address, age, hobby)  # 这个占位符的方法是不是很麻烦？
# s0 = "我叫%s" % name  # 当只有一个占位符的时候，这个方法就比较方便了
# s1 = "我叫{0}，我住在{1}，我今年{2}岁，我的爱好是{3}".format(name, address, age, hobby)  # 这两种方法是不是还是很麻烦？看下面这个
# s2 = f"我叫{name}，我住在{address}，我今年{age}岁，我的爱好是{hobby}"  # f-string在python 3.6以上引用了这个简化方法
# print(s)
# print(s0)
# print(s1)
# print(s2)
# 2. 索引和切片
# 索引：按照位置提取元素
# s = "我叫周杰伦"
# 可以采用索引的方式提取某一个元素（文字）
# print(s[3])  # 索引都是从0开始数数
# print(s[0])
# print(s[-1])  # “-”表示从后往前数（倒数）

# 切片：从一个字符串中提取一部分内容（断章取义）
# s = "我叫周杰伦，你呢？你叫周润发吗？"

# print(s[3:6])  # 从索引3位置进行切片，切到6结束，有一个坑：切片取不到第二个位置的元素。
# 语法：s[start:end] 从start到end进行切片，但不包含end位置[start, end)
# print(s[0:5])
# print(s[:5])  # 如果start是从开头进行切片，可以省略不写
# print(s[6:])  # 从start位置进行切片，到结尾进行切片，可以省略end
# : 如果左右两端有空白，则表示从开头或到结尾
# print(s[:])

# print(s[-3:-1])  # 目前还只能从左往右切片
# print(s[-1:-3])  # 没结果，因为切片是左闭右开，所以这里又是坑！


# s = "我爱你"
# 可以给切片添加步长来控制切片的方向
# print(s[::-1])  # -1表示倒着切片，从后往前，从0开始，到-1结束，步长为-1，所以是倒着切片
# 语法：s[start:end:step] 从start位置开始切片，到end结束，步长为step

# s = "abcdefghijklmnopqrstuvwxyz"
# print(s[2:11:3])
# print(s[-1:-10:-3])


# 3.字符串的常规操作
# 字符串的操作一般不会对原字符串产生影响，而是返回一个新的字符串
# 3.1 字符串大小转换
# s = "python"
# s1 = s.capitalize()   # 将字符串的第一个字母大写，其他字母小写
# print(s1)
#
# s = "I have a dream!"
# s1 = s.title()  # 将字符串中每个单词的第一个字母大写，其他字母小写
# print(s1)
#
# s = "I HAVE A DREAM!"
# s1 = s.lower()  # 将字符串全部转换为小写
# print(s1)
#
# s = "i have a dream!"
# s1 = s.upper()  # 将字符串全部转换为大写
# print(s1)

# 如何忽略大小写来进行判断
# verify_code = "xAd1"
# user_input = input(f"请输入验证码({verify_code})：")
# if user_input.upper() == verify_code.upper():
#     print("验证码正确")
# else:
#     print("验证码错误")


# 3.2 替换和切割（*）
# strip()
# s = "     你好，   我叫   周杰伦    "
# s1 = s.strip()
# print(s1)

# 比如
# username = input("请输入用户名：")
# password = input("请输入密码：")
# if username == "admin" and password == "123456":
#     print("登录成功")
# else:
#     print("登录失败")

# # replace(old, new) 字符串替换
# s = "你好啊，我叫周杰伦"
# s1 = s.replace("周", "周杰伦")
# print(s1)
#
# a = "hello i am a good man!"
# a1 = a.replace(" ", "")  # 去掉所有的空格
# print(a1)
#
# split(用什么切割)  # 字符串切割，用什么切，就会损失掉这个字符
# a = "python_java_c_c#_javascript"
# lst = a.split("_")  # 切割之后的结果会放在列表中
# print(lst)
# lst = a.split("_java_")
# print(lst)

# replace(),  split(), strip()     ==> 记住


# ===============================================
# 3.4 查找和判断
# 查找
# s = "你好啊，我叫蔡徐坤"
# ret = s.find("蔡徐坤12312")  # 如果找到了，返回索引，找不到返回-1
# print(ret)
# ret = s.index("蔡徐坤")  # 如果找到了，返回索引，找不到会报错
# print(ret)

# print("蔡徐坤" in s)  # in可以做条件上的判断
# print("蔡徐坤" not in s)  # not in判断是否不在

# 判断
# name = input("请输入你的名字：")
# # 判断你是不是姓张
# if name.startswith("张"):  # 判断字符串是否以xxxx开头，endswith()判断字符串是否以xxxx结尾
#     print("你姓张")
# else:
#     print("你不姓张")
#

# money = input("请输入你兜里的钱：")
#
# if money.isdigit():  # 判断字符串是否由整数组成
#     money = int(money)
#     print("可以花钱了")
# else:
#     print("对不起，您输入有误......")


# startswith(), endswith(), isdigit(), in, not in, find()


# ==================================================
# 3.5 补充和总结
# s = "hello"
# print(len(s))  # length  长度
#
# # join()
# s = "python_java_c_javascript"
# lst = s.split("_")
# print(lst)
#
# lat = ['赵本山',  '周杰伦', '王力宏']
# # 用_把上面的人的名字连接起来
# s = "_".join(lat)
# print(s)

# 总结：
"""
1. f'{变量}' 格式化一个字符串
2. 索引和切片：
    索引：从0开始. []
    切片：s[start:end:step],end位置的数据永远都拿不到
3. 相关操作:
    字符串操作对原字符串不会发生改变的。
    1. upper() 在需要忽略大小写的时候使用
    2. strip() 可以去掉字符串两边的空白(空格，\t,\n)
    3. replace(old, new) 字符串替换
    4. split(sep) 字符串切割，切割之后的结果会放在列表中
    5. join(sep, ) 拼接一个列表中的内容成为新的字符串
    6. startswith() 判断字符串是否以xxxx开头
    7. len(sep) 字符串长度(内置函数)

    字符串的循环和遍历
    for i in s:
        print(c)  字符串中的每一个字符串

    关于in:
        1. 判断xxx是否存在xxx中出现了
        2. for循环

"""

# ===================================
# 不计分

# 窗口配置
SCREEN_WIDTH = 1500
SCREEN_HEIGHT = 900

# 物理参数
PLAYER_BASE_SPEED = 20
PLAYER_BOOST_MULTIPLIER = 1.8  # 加速倍率
BALL_RADIUS = 20
BOUNCE_STRENGTH = 0.85
COLLISION_FORCE = 28
BLUE_ACC = 0.99  # 篮球加速度调整
BLUE_SPEED_CAP = 25  # 保持原最大速度
BOOST_TIME_THRESHOLD = 27  # 60帧=1秒

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 游戏对象
player = pygame.Rect(750, 750, 50, 50)
blue_pos = Vector2(750, 750)
blue_vel = Vector2()
yellow_pos = Vector2(SCREEN_WIDTH // 2, 200)
yellow_vel = Vector2(3, 0)

# 按键计时器
key_hold_timer = {pygame.K_UP: 0, pygame.K_DOWN: 0, pygame.K_LEFT: 0, pygame.K_RIGHT: 0}


def reset_ball():
    global blue_pos, blue_vel
    blue_pos = Vector2(750, 750)
    angle = math.radians(random.uniform(0, 360))
    blue_vel = Vector2(15 * math.cos(angle), 15 * math.sin(angle))  # 加强初始速度


def check_collision(rect, circle_pos, radius):
    closest_x = max(rect.left, min(circle_pos.x, rect.right))
    closest_y = max(rect.top, min(circle_pos.y, rect.bottom))
    dx = circle_pos.x - closest_x
    dy = circle_pos.y - closest_y
    return dx ** 2 + dy ** 2 < radius ** 2


def check_ball_collision(pos1, pos2, radius):
    return pos1.distance_to(pos2) < radius * 2


def handle_boundary(pos, vel, radius):
    if pos.x < radius:
        pos.x = radius
        vel.x = abs(vel.x) * BOUNCE_STRENGTH
    elif pos.x > SCREEN_WIDTH - radius:
        pos.x = SCREEN_WIDTH - radius
        vel.x = -abs(vel.x) * BOUNCE_STRENGTH

    if pos.y < radius:
        pos.y = radius
        vel.y = abs(vel.y) * BOUNCE_STRENGTH
    elif pos.y > SCREEN_HEIGHT - radius:
        pos.y = SCREEN_HEIGHT - radius
        vel.y = -abs(vel.y) * BOUNCE_STRENGTH * 1.2
    return pos, vel


def update_blue_ai():
    global blue_vel
    target_dir = (yellow_pos - blue_pos).normalize()
    blue_vel += target_dir * BLUE_ACC

    # 速度限制
    if blue_vel.magnitude() > BLUE_SPEED_CAP:
        blue_vel = blue_vel.normalize() * BLUE_SPEED_CAP

    # 保持0.99速度衰减
    blue_vel *= 0.99


def update_yellow_ai():
    global yellow_vel
    escape_dir = (yellow_pos - player.center).normalize() + (
            yellow_pos - blue_pos
    ).normalize()
    escape_dir = escape_dir.normalize()

    # 边缘逃生
    if yellow_pos.x < 150 or yellow_pos.x > SCREEN_WIDTH - 150:
        escape_dir.y += 0.8 * (-1 if yellow_pos.y < SCREEN_HEIGHT / 2 else 1)
    if yellow_pos.y < 150 or yellow_pos.y > SCREEN_HEIGHT - 150:
        escape_dir.x += 0.8 * (-1 if yellow_pos.x < SCREEN_WIDTH / 2 else 1)

    yellow_vel += escape_dir * 0.035  # 加强逃生加速度
    if yellow_vel.magnitude() > 35:  # 提高黄球速度上限
        yellow_vel = yellow_vel.normalize() * 35


# 游戏主循环
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            reset_ball()

    # 更新按键计时
    keys = pygame.key.get_pressed()
    for key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
        key_hold_timer[key] = key_hold_timer[key] + 1 if keys[key] else 0

    # 玩家移动计算
    y_speed = PLAYER_BASE_SPEED
    x_speed = PLAYER_BASE_SPEED

    # 垂直方向加速
    if keys[pygame.K_UP] and key_hold_timer[pygame.K_UP] > BOOST_TIME_THRESHOLD:
        y_speed *= PLAYER_BOOST_MULTIPLIER
    if keys[pygame.K_DOWN] and key_hold_timer[pygame.K_DOWN] > BOOST_TIME_THRESHOLD:
        y_speed *= PLAYER_BOOST_MULTIPLIER

    # 水平方向加速
    if keys[pygame.K_LEFT] and key_hold_timer[pygame.K_LEFT] > BOOST_TIME_THRESHOLD:
        x_speed *= PLAYER_BOOST_MULTIPLIER
    if keys[pygame.K_RIGHT] and key_hold_timer[pygame.K_RIGHT] > BOOST_TIME_THRESHOLD:
        x_speed *= PLAYER_BOOST_MULTIPLIER

    # 应用移动
    player.y = max(
        0,
        min(
            SCREEN_HEIGHT - 50,
            player.y - keys[pygame.K_UP] * y_speed + keys[pygame.K_DOWN] * y_speed,
        ),
    )
    player.x = max(
        0,
        min(
            SCREEN_WIDTH - 50,
            player.x - keys[pygame.K_LEFT] * x_speed + keys[pygame.K_RIGHT] * x_speed,
        ),
    )

    # 更新篮球
    update_blue_ai()
    blue_pos += blue_vel
    blue_pos, blue_vel = handle_boundary(blue_pos, blue_vel, BALL_RADIUS)

    # 更新黄球
    update_yellow_ai()
    yellow_pos += yellow_vel
    yellow_pos, yellow_vel = handle_boundary(yellow_pos, yellow_vel, BALL_RADIUS)

    # 碰撞处理
    if check_ball_collision(blue_pos, yellow_pos, BALL_RADIUS):
        collision_dir = (yellow_pos - blue_pos).normalize()
        blue_vel = -collision_dir * COLLISION_FORCE * 0.7
        yellow_vel = collision_dir * COLLISION_FORCE * 1.4

    if check_collision(player, yellow_pos, BALL_RADIUS):
        dir = (yellow_pos - player.center).normalize()
        yellow_vel = dir * COLLISION_FORCE * 1.2

    if check_collision(player, blue_pos, BALL_RADIUS):
        dir = (blue_pos - player.center).normalize()
        blue_vel = dir * COLLISION_FORCE * 0.8

    # 渲染
    screen.fill("black")
    pygame.draw.rect(screen, "red", player)
    pygame.draw.circle(screen, "blue", blue_pos, BALL_RADIUS)
    pygame.draw.circle(screen, "yellow", yellow_pos, BALL_RADIUS)
    pygame.display.flip()
    clock.tick(60)

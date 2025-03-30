a = 100
b = 200
print(a, b, '装逼，我让你飞起来')#这是一个简单的代码
# ================================================
a = 50
b = 100
c = 200
print(a * b / c)
print(a + b)
print("你好，晚上好")
# ================================================
print('b')
print(chr(98))
print('c')
print(chr(67))
print(8)
print(chr(56))
print('[')
print(chr(91))
# ================================================
print(ord('你'), ord('好'))
print(chr(20320), chr(22909))
# ================================================
flag = False
name = 'liunx'
if name == 'liunx':        #判断变量是否为 python
    flag = True            #条件成立时设置标志为真
    print('你好啊，新同学！')  #并输出欢迎信息
else:
    print(name)            #条件不成立时输出变量名称
# ===================================================
num = 0
if num == 3:        #判断Num的值
    print('boss')
elif num == 2:
    print('user')
elif num == 1:
    print('worker')
elif num == 0:
    print('nimalege')
elif num < 0:       #值小于零时输出
    print('error')
else:
    print('roadman')#条件不成立时输出
# ===============================================
cao = 9
if cao >= 0 and cao <= 10:#判断值是否在0~10之间
    print('你好，你好，你好！')
#输出结果：我不好

cao = 10
if cao < 0 and cao > 10:#判断值是否在小于0或大于10
    print('我上早八')
else:
    print('宝了个贝的，这是给我干那来了，这还是国内吗？')
#输出结果：孩子，这并不好笑

cao = 8
#判断值是否在0~5或者10~15之间
if (cao >= 0 and cao <= 5)or(cao >= 10 and cao <= 15):
    print('我测你温码')
else:
    print('我是丁真，这是我的好朋友芝士雪豹。')
#输出结果：嗷呜~ 雪豹别叫!
# ==============================================
var = 100
if var == 100:
    print("太好啦，是烧鸡，我们没救了！")
    print("心还没有悬着就去世了！")
蛊真人 = '大专巅峰'
if 蛊真人 == '大专巅峰':
    print("“你到底干了什么，你不跟我们干，我们以后怎么赚大钱”室友跺着脚恶狠狠地瞪着他。")
    print("他淡然一笑“很简单，我进厂不就是了”说完，他的气息不再掩饰，显露而出，大专巅峰！！一瞬间，流水线再次一寂。")
    print("我乃大专巅峰！何人敢叼我，何人能叼我！他口中低吟道：")
    print("电子厂中寒风吹，流水线上大神归")
    print("一号工位黑奴泪，褪去校服人向北")
    print("无休倒班万人退，三千工资空落泪")
    print("宿命天成当厂妹，本科悔而我不悔!")
    print("早岁已知挣钱艰，仍许资本荡人间")
    print("十年苦读身如絮，无尘车间客独行")
    print("千磨万击手铸铁，殚精竭虑打工件")
    print("今朝人向工位处，打件打人还打天")
    print("从今以后，他就彻底从一位学生变成一位打工人，可以堂堂正正的打螺丝，造福车间了，工友们的历史，资本家们的历史不得不记载他的名字，至此他和数百位工友并肩，宛若大日光照千古，其余同学无论多么豪杰英雄，皆为繁星。")
大专生 = '发言'
if 大专生 == '发言':
    print('不过是些许风霜罢了')
    print('面对凶险万分的流水线，不退反进，仰天大喝：件来！')
    print('今朝剑指叠云处，炼蛊炼人还炼天')
# ================================================
age = input('打出你的年龄: ')#输入你的年龄
print(age)#输出你的输入
# ================================================
x = 10
y = 5
s = x * y
print(s)
# ================================================
result = '我' + '和' + '你'
print(result)#输出我和你
# ================================================
a,b,c = 1,2,'jojo'
print(a, b, c)
# ================================================
str = '你好啊，外邦的旅客！'
print(str)
print(str[0])
print(str[1])
print(str[2:5])
print(str[2:])
print(str * 2)
print(str + "end")
print(str[:7])
# ===============================================
list = [ 'What can I say?', 786, 2.23, 'jojo', 70.2]
tinylist = [123, 'jojo']
print(list)
print(list[0])
print(list[1:3])
print(list[2:])
print(tinylist * 2)
print(list + tinylist)
# ===============================================
dict = {}
dict['我来助你！'] = "广智救我！"
dict['出门撞大运'] = "新年快乐！"

tinydict = {'米饭仙人': '风灵月影', '刚满18岁':114514,'我这一生如履薄冰':'菜就多练'}


print(dict['我来助你！'])#字典中的键值对
print(dict['出门撞大运'])#字典中的键值对
print(tinydict)#字典中的键值对
print(tinydict.keys())#字典的键
print(tinydict.values())#字典的值
print(tinydict.items())#字典的键值对
print(dict.items())#字典的键值对
print(dict.keys())#字典的键
print(dict.values())#字典的值

# ===============================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = '就凭你也配直视我！'#神
b = '把头低下！'#精
list = ['诶呀', '真的是你呀', '哈哈', '嗐呦', 'baby'];#练习生

if (a in list):#如果，“神”在“练习生”里。就告诉你，勇敢去做，否则，没有不可能
    print("勇敢去做")#对
else:#不
    print("没有不可能")#对

if (b not in list):#如果“神精”在“练习生”里，就偷懒
    print("2 - 变量 b 不在给定的列表中 list 中")#懒
else:#否则
    print("2 - 变量 b 在给定的列表中 list 中")#偷

# 修改变量 a 的值
a = '真的是你呀'#练习时长两年半
if (a in list):#如果你有两年半的练习
    print("3 - 变量 a 在给定的列表中 list 中")#你就练习了两年半
else:#杂鱼
    print("3 - 变量 a 不在给定的列表中 list 中")#错过就是失去，你明白了吗。
# ===========================================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = 20#变量为20
b = 10#变量为10
c = 15#变量为15
d = 5#变量为5
e = 0#变量为0

e = (a + b) * c / d  # ( 30 * 15 ) / 5
print("(a + b) * c / d 运算结果为：", e)#输出上面的式子

e = ((a + b) * c) / d  # (30 * 15 ) / 5
print("((a + b) * c) / d 运算结果为：", e)#费手

e = (a + b) * (c / d);  # (30) * (15/5)
print("(a + b) * (c / d) 运算结果为：", e)#一对对照组

e = a + (b * c) / d;  # 20 + (150/5)
print("a + (b * c) / d 运算结果为：", e)#看，电灯泡
# =======================================================
#!/usr/bin/python

count = 0#设定函数值为0
while (count < 9):#在当函数值小于9的条件下循环输出以下内容
    print('The count is:', count)#输出，包含下一个变量
    count = count + 1#每一次循环都加1

print("Good bye!")#不成熟的解释
# =========================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

var = 1
while var == 1:  # 该条件永远为true，循环将无限执行下去
    num = input("随便 :")  #随便写一个，回车
    print("写了个寂寞: ", num)#输出你刚刚写下的东西
    if num == '1314':  # 当你输入一生一世时，循环终止
        break
print("拜拜!")#友好的再见
# =======================================
#!/usr/bin/python

count = 0
while count < 5:
    print(count, " is  less than 5")
    count = count + 1
else:
    print(count, " is not less than 5")
# ==========================================
#!/usr/bin/python
import time

keep_running = True
start_time = time.time()

while keep_running:
    print('Given flag is really true!')
    # 5 秒后终止循环
    if time.time() - start_time > 5:
        keep_running = False
    time.sleep(0.1)  # 降低 CPU 占用

print("Good bye!")
# ===================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for letter in '一个字，绝':  # 第一个实例
    print("看看看看: %s" % letter)

fruits = ['唱', '跳', 'rap','篮球']
for fruit in fruits:  # 第二个实例
    print('真的是你呀，哈哈！: %s' % fruit)

print("baybay!")
# ==================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

fruits = ['鸡', '你', '太美']
for index in range(len(fruits)):
    print('真的是你呀！哈哈 ： %s' % fruits[index])

print("beybey!")
# ====================================================
#!/usr/bin/python
# -*- coding: UTF-8 -*-

for num in range(10, 20):  # 迭代 10 到 20 (不包含) 之间的数字,简单来说就是10~19
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)

# !/usr/bin/python
# -*- coding: UTF-8 -*-

i = 2
while (i < 100):
    j = 2
    while (j <= (i / j)):
        if not (i % j): break
        j = j + 1
    if (j > i / j): print(i, " 是素数")
    i = i + 1

print("Good bye!")
# ==============================================
apple = 'eat'  #吃苹果
kill = 'eat'  # 修正了这里，将 kill 的值改为 'eat'
I = 'you'
kiss = 'you'

# 检查条件是否满足
if apple == kill and I == kiss:
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
elif apple == kiil and I != kiss:
    print('一袋米引发的战争')
'''试了三次啊，三次，终于成功了'''
# ========================================================
a = input("第一个数字：")
b = input("第二个数字：")
# print(type(a))#查看变量类型
a = int(a)
b = int(b)
# print(type(a))
print(a+b)
# ================================
money = int(input("交出你的money，哈哈哈: "))#要钱
if money >= 500:
    print("太好啦，是钱，我们有救了！")#太好了，是甲方
else:
    print("太好了，让我们进入米奇妙妙屋。")#（勉强的笑容）
if money >= 1000:
    if money > 1000 and money < 5000:
        print('加油加油！')#厉害了我的哥
    elif money ==1000:
        print('有所懈怠了呀。')#基本满足
    if money == 1000:
        print('刚刚好，是不是故意的？')#黑暗森林，有着猜疑链
if money >= 500 and money <= 1000:
    if money == 500:
        print('回家吧，你也不希望在外面出丑吧？')#可以吃饭
    if money == 1000:
        print('不是故意的，就是有意的！')#自问自答
    if money > 500 and money < 1000:
        print('你的想法真是让人捉摸不透啊！')#呀呀呀呀
    else:
        print('嘿，你瞅啥呢，我是你蝶！')#哎呀呀
# ================================================
a = int(input("来来来（数字，不要提前回车）："))
b = 0
while b <= 100: #用while循环100次，哈哈哈
    print(a)
    b += 1
    a += b
    print(b)
    a -= b #还是徒劳吗？
    # break 用break直接结束循环
# ====================================时间戳的运用示例
import time

# 获取当前时间戳（秒级时间戳）
timestamp = time.time()
print("当前时间戳（秒）:", timestamp)#时间戳的英文

# 获取当前时间戳（毫秒级时间戳）
timestamp_ms = int(round(time.time() * 1000))
print("当前时间戳（毫秒）:", timestamp_ms)#横杠加ms


import time
from datetime import datetime#运用了时间数据

# 将秒级时间戳转换为日期时间
timestamp = time.time()
dt = datetime.fromtimestamp(timestamp)
print("从时间戳转换为日期时间:", dt)

# 将毫秒级时间戳转换为日期时间
timestamp_ms = 1672531200000  # 示例毫秒级时间戳
dt_ms = datetime.fromtimestamp(timestamp_ms / 1000)
print("从毫秒级时间戳转换为日期时间:", dt_ms)


from datetime import datetime

# 将日期时间转换为秒级时间戳
dt = datetime.now()
timestamp = dt.timestamp()
print("从日期时间转换为时间戳（秒）:", timestamp)

# 将日期时间转换为毫秒级时间戳
timestamp_ms = int(dt.timestamp() * 1000)
print("从日期时间转换为时间戳（毫秒）:", timestamp_ms)


import time
from datetime import datetime

# 获取当前时间戳并格式化为日期时间字符串
timestamp = time.time()
formatted_time = datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")
print("格式化的时间:", formatted_time)


from datetime import datetime

# 计算两个时间戳之间的时间差
timestamp1 = time.time()
time.sleep(2)  # 模拟等待2秒
timestamp2 = time.time()

# 计算时间差（秒）
time_diff = timestamp2 - timestamp1
print("时间差（秒）:", time_diff)


from datetime import datetime, timedelta

# 创建一个日期时间对象
dt = datetime.now()#现在
print("当前日期时间:", dt)

# 添加时间
new_dt = dt + timedelta(days=1, hours=2, minutes=30)
print("添加时间后:", new_dt)

# 减去时间
old_dt = dt - timedelta(days=1)
print("减去时间后:", old_dt)


from datetime import datetime

# 定义两个日期时间
start_time = datetime(2024, 1, 1)
end_time = datetime(2024, 1, 15)

# 计算时间戳差
time_diff = (end_time - start_time).total_seconds()
print("两个日期之间的时间戳差（秒）:", time_diff)
# ========================================================时间控制循环示例（好玩）
# 使用 time.time() 来控制循环时间
import time

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
from datetime import datetime, timedelta

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


# # 使用 signal 模块（仅限 Unix 系统）
# import signal
# import time
#
# # 定义一个标志变量，用于控制循环
# stop_loop = False
#
# # 定义信号处理函数
# def handle_timeout(signum, frame):
#     global stop_loop
#     print("时间限制已到，停止循环。")
#     stop_loop = True
#
# # 设置信号处理
# signal.signal(signal.SIGALRM, handle_timeout)
# signal.alarm(5)  # 设置 5 秒后发送 SIGALRM 信号
#
# try:
#     while not stop_loop:
#         print("循环正在运行...")
#         time.sleep(1)  # 模拟每次循环耗时 1 秒
# finally:
#     signal.alarm(0)  # 取消定时信号

# 使用多线程
import threading
import time

# 定义一个标志变量，用于控制循环
stop_loop = False

# 定义一个函数来控制循环时间
def stop_after_timeout(timeout):
    global stop_loop
    time.sleep(timeout)
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
import asyncio

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
    print("这一次，请确定:",i)

for i in range(10): #从0数到10，但不包含10
    print(i)

for i in range(3,10): #3~9
    print(i)

i = 1
while i <= 10:#成立
    print(i)
    i += 2#由i = i + 2

for i in range(1,10,2):#1~9,跳过2
    print(i)#就是只输出1 3 5 7 9

x = 10
if x > 5:
    pass #跳过，下次想好了再补充
print("吹牛逼呢，见过吗，这叫俄罗斯大贝塔，你就只能看着我骑")
# ============================================================
import time  #使用标志变量 + 时间戳（无需多线程）

start_time = time.time()
timeout = 5  # 5秒后停止

while True:
    # 循环内执行你的操作
    print("循环运行中...")
    time.sleep(1)  # 模拟操作耗时

    # 检查是否超时
    if time.time() - start_time > timeout:#用现在比较过去，你还会犹豫吗？
        print("已超时，停止循环")
        break

import time    #使用多线程 + 定时器（精确控制）
import threading

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
a = 10
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
print(10/3) #它的输出的最后一位存在误差，说明关于无穷，计算机也是只能给出不准确的数
#还有，小数的数据范围是无限的，而整数会在某一个特定区间内是可以清楚表示的
#就像你与你命中注定的人的距离，处于小数时，距离是可以无限近和无限远的。但是，处于整数时，在一瞬间，你们两个的关系就明确了
#计算机是一款二进制产品，语言基础就：0,1，人家本来就难，不要强迫别人，所以，计算机在表示一个小数时是会有误差的
bool
#===============================================================
#蛊界的那些事
import time
血颅蛊 = '众人所望'
方源 = '哭泣'
if 血颅蛊 == '众人所望':
    print('古月族长：')
    print('''方源，你不要再妇人之仁了。
快对我们使用血颅蛊，
再晚就来不及了，
你难道要看着我们古月一族，
彻底消失吗？''')
    time.sleep(1)
if 方源 == '哭泣':
    print('方源：')
    print('''不，族长爷爷，
我不能这样，
我不能这样！
我要陪你们一起战斗，我们还有希望的！''')
    time.sleep(1)
if 血颅蛊 == '众人所望' and 方源 == '哭泣':
    print('古月族长：')
    print('''没有机会了。
吐血；
古月方源，
我以古月一族之长的身份命令你
咳血*2；
立刻使用血颅蛊，活下去...重振我古月一族
否则，你再也不是我古月一族之人！''')
    time.sleep(0.5)
    print('方源爆发：')
    print('''族长爷爷，族人们，
你们放心，我一定会重振古月一族的辉煌，
我会为你们报仇，还要从仙鹤门手中救出弟弟
仙鹤门，我古月方源对天发誓，有朝一日，定让你们鸡犬不留...''')
    time.sleep(1)
蛊真人 = '方源诵诗'
if 蛊真人 == '方源诵诗':
    print('''落魄谷中寒风吹，春秋蝉鸣少年归。
荡魂深处石人泪，定仙游走魔向北。
逆流河上万仙退，爱情不敌坚持泪。
宿命中成命中败，仙尊悔，而我不悔！''')
    time.sleep(1)
方源 = '历史，如果有用还要我有什么用！！！'
if 方源 == '历史，如果有用还要我有什么用！！！':
    print('10岁', '青梅竹马，献祭自己，为主角增长修为 三转',
'\n15岁', '全族为了保住家族火种，强行为主角提升资质，甲等',
'\n18岁', '为保护八十八角真阳楼，无奈放弃前途成仙，',
'\n20岁', '被尊者作为蛊虫实验品，天妒',
'\n25岁', '被双尊合力打杀，弥留之际，光阴长河中传来一句诛心之言',
'\n你... 可曾有一丝后悔',
'\n少年微笑' + ' 不过是些许风霜罢了' + ' 维护他人，无悔'
'\n顷刻间，尊者，成', )
print('为什么都说' + ' 白凝冰' + ' 实际上才是蛊真人笔下的第一女主呢？',
'\n因为她说：',
'\n这个蛊界好不公平',
'我陪你从古月山寨一直走到了三王山，'
'见证你以蛊师之身，'
'练出了六转仙蛊，'
'可是几年后出现的星宿仙尊，'
'却轻易地夺走了那个最好的你，'
'未来会更好的你'
'爱情，真的要这么毫无道理吗？'
'对于蛊界，你是冷酷残忍的炼天魔尊，'
'但是对我来说，你就是那个只为造福世界，恢复五域和谐的大爱仙尊啊！',
'''4月23，和方源一起吃冰淇淋，甜甜的很好吃，方源还帮我擦嘴
4月24，和方源去商量山，世界最暖和的地方在商家的演武场
4月25，和方源去三王山，有人在那里炼仙蛊，不知道会是什么呢
4月26，和方源去天庭，星宿仙尊很可怕，但是有方源在，所以不可怕
方源最好了，冰冰只爱方源''')
time.sleep(1)
print('''女童：哎呀，我的玩具
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
今朝陀出风云起，转蛊转人还转天！”''')
# ==============================================================
import turtle

# 设置屏幕
screen = turtle.Screen()#screen是变量
screen.setup(600, 400)#设置屏幕大小
screen.bgcolor("red")#设置背景颜色

# 创建画笔
pen = turtle.Turtle()#pen是变量
pen.speed(10)#设置画笔速度为10
pen.penup()#设置画笔抬起

# 绘制大五角星
def draw_star(x, y, size):
    #定义函数draw_star,def是声明后方的代码是函数
    pen.goto(x, y)#设置画笔位置为x,y
    pen.pendown()#设置画笔落下
    pen.color("yellow")#设置画笔颜色为黄色
    pen.begin_fill()#开始填充
    for _ in range(5):#循环五次
        pen.forward(size)#画笔向前移动size
        pen.right(144)#设置画笔向右旋转144度
    pen.end_fill()#结束填充
    pen.penup()#设置画笔抬起

# 绘制大五角星
draw_star(-200, 100, 100)#调用函数draw_star

# 绘制四个小五角星
def draw_small_star(x, y, size, angle):
    #定义函数draw_small_star
    pen.goto(x, y)#设置画笔位置为x,y
    pen.setheading(angle)#设置画笔朝向angle度
    pen.pendown()#设置画笔落下
    pen.color("yellow")#设置画笔颜色为黄色
    pen.begin_fill()#开始填充
    for _ in range(5):#循环五次
        pen.forward(size)#设置画笔向前移动size
        pen.right(144)#设置画笔向右旋转144度
    pen.end_fill()#结束填充
    pen.penup()#设置画笔抬起

# 绘制四个小五角星
draw_small_star(-100, 160, 30, 30)#调用函数draw_small_star
draw_small_star(-60, 120, 30, 0)#调用函数draw_small_star
draw_small_star(-60, 60, 30, -30)#调用函数draw_small_star
draw_small_star(-100, 20, 30, -60)#调用函数draw_small_star

# 隐藏画笔
pen.hideturtle()

# 结束
turtle.done()#阻塞程序并保持窗口打开，直到用户手动关闭
turtle.mainloop()
# ===============================================================
# from turtle import*#可以不用导入，直接用turtle
import turtle
import turtle as t
import time as ti
'''t.speed(0)    # 设置最快速度
t.tracer(0)   # 关闭自动刷新
# ==================================
#四个圆
a = 1
while a <= 4:
    t.circle(100)
    t.right(90)
    a += 1

t.update()     # 最终刷新画面
ti.sleep(5)    # 保持窗口显示（可选）

# t.circle(100)
# t.left(180)
# ===================================
#球
for i in range(100):
    t.circle(100)
    t.right(91)
t.done()
# ===================================
#四方相回
for i in range(100):
    t.circle(i)
    t.right(91)
t.done()
# ==================================
#彩色的圆
for i in range(100):
    t.circle(i)
    t.right(91)
    t.color("red")
    t.color("blue")
    t.color("green")
    t.color("yellow")
    t.color("pink")
    t.color("purple")
    t.color("orange")
    t.color("black")
    t.color("white")
t.done()
# ==================================
#不好看
import turtle as t

# 颜色配置优化方案
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
t.speed(0)  # 设置最快绘制速度

for i in range(100):
    # 通过取余实现颜色循环
    t.color(colors[i % len(colors)])
    t.circle(i)
    t.right(91)

t.done()
# ==================================
#好看吗？
import turtle as t
import random

# 方式1：使用随机RGB颜色（更丰富的色彩）
t.colormode(255)  # 必须设置颜色模式
t.speed(0)

for i in range(100):
    # 生成随机RGB颜色
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    t.color((r, g, b))

    t.circle(i)
    t.right(91)

t.done()
# ==================================
#蓝球
t.color('blue')
for i in range(100):
    t.circle(i)
    t.right(78)
# ==================================
#奥运五环
t.pensize(9)

t.color('black')
t.circle(75)

t.penup()
t.goto(-180,0)
t.pendown()
t.color('blue')
t.circle(75)

t.penup()
t.goto(180,0)
t.pendown()
t.color('red')
t.circle(75)

t.penup()
t.goto(90,-75)
t.pendown()
t.color('green')
t.circle(75)

t.penup()
t.goto(-90,-75)
t.pendown()
t.color('yellow')
t.circle(75)

t.color('black')
t.penup()
t.goto(-100,180)
t.pendown()
t.write('北京 2020',font=('kaiti',32))
t.hideturtle()
# ==================================
#美国盾牌
t.penup()
t.goto(0,-200)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(200)
t.end_fill()

t.penup()
t.goto(0,-150)
t.pendown()
t.color('white')
t.begin_fill()
t.circle(150)
t.end_fill()

t.penup()
t.goto(0,-100)
t.pendown()
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(0,-50)
t.pendown()
t.color('blue')
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-40,10)
t.pendown()

t.color('white')

t.begin_fill()

for i in range(5):
    t.forward(80)
    t.right(144)

t.end_fill()

t.hideturtle()
# =================================
#彩球飘飘

#随机数
import random

t.colormode(255)
t.speed(0)

for i in range(20):
    red = random.randint(0,255)#在这里调颜色
    green = red = random.randint(0,255)
    blue = red = random.randint(0,255)

    x = random.randint(-220,220)
    y = random.randint(-100,220)

    t.penup()
    t.goto(x,y)
    t.pendown()

    t.color(red,green,blue)

    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.right(90)
    t.forward(30)
    t.left(90)
t.done()
#RGB red green blue'''
#==================================
#繁星满天
import random
t.bgcolor('black')

t.speed(0)
t.colormode(255)

t.pensize(250)
for i in range(10):
    t.goto(-500,300-i*100)
    t.color(i*20,i*20,i*20)
    t.forward(1000)

for x in range(8):
    if x%2==0:
        t.left(30)
    else:
        t.right(120)
    t.forward(50)
for i in range(20):
    x = random.randint(-400,400)
    y = random.randint(-100,350)
    e = random.randint(1, 15)
    def drawStar():
        t.begin_fill()
        for i in range(4):
            t.forward(e)
            t.left(30)
            t.forward(e)
            t.right(120)
        t.end_fill()

    t.pensize(5)
    t.penup()
    t.goto(x, y)
    # t.goto(150,150)
    t.pendown()
    red = random.randint(180,255)
    green = random.randint(180,255)
    blue = 0
    t.color(red, green, blue)
    drawStar()
#===================================
#如果柱状图报错，就用这个
import matplotlib
matplotlib.use('TkAgg')  # 或者 'Qt5Agg'
import matplotlib.pyplot as plt
import numpy as np

# 生成随机数据
var = np.random.randint(1, 10, 10)

# 绘制柱状图
plt.bar(range(len(var)), var)

# 显示图表
plt.show()
# ==================================
# 没有输出看看这个
def fire(n, c=1):
    # 参数类型校验
    if not isinstance(n, int) or not isinstance(c, int):
        raise TypeError("参数必须是整数")

    # 参数范围校验
    if n < 1 or c < 1 or c > n:
        raise ValueError("参数范围无效：n需≥1且1≤c≤n")

    # 修正金字塔方向
    for current in range(c, n + 1):
        spaces = ' ' * (n - current)  # 修正空格计算逻辑
        stars = '*' * (2 * current - 1)  # 修正星号计算逻辑
        print(spaces + stars)


fire(5)
# ==================================
#可玩版本，到底哪里错了！
import pygame

# 初始化配置
pygame.init()
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# 创建矩形（修正类名和变量名）
square_pos = pygame.Rect(175, 75, 50, 50)  # 居中初始位置

running = True
while running:
    # 正确处理事件队列
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 获取按键状态
    keys = pygame.key.get_pressed()
    move_speed = 20  # 统一速度变量

    # 处理移动（带边界检测）
    new_x = square_pos.x
    new_y = square_pos.y

    if keys[pygame.K_UP]:
        new_y = max(0, square_pos.y - move_speed)
    if keys[pygame.K_DOWN]:
        new_y = min(screen.get_height() - 50, square_pos.y + move_speed)
    if keys[pygame.K_LEFT]:
        new_x = max(0, square_pos.x - move_speed)
    if keys[pygame.K_RIGHT]:
        new_x = min(screen.get_width() - 50, square_pos.x + move_speed)

    square_pos.topleft = (new_x, new_y)

    # 渲染逻辑
    screen.fill("black")
    pygame.draw.rect(screen, "red", square_pos)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
# =================================
#有小球版本
import pygame

# 常量配置
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SQUARE_SIZE = 50
MOVE_STEP = 20

# 圆形物理参数
CIRCLE_RADIUS = 20
GRAVITY = 0.5
DAMPING = 0.85  # 能量衰减系数
BOUNCE_STRENGTH = 0.8  # 碰撞反弹强度
MAX_Y_SPEED = 15  # 防止速度过大穿透地面

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 矩形初始化
square_pos = pygame.Rect(
    (SCREEN_WIDTH - SQUARE_SIZE) // 2,
    (SCREEN_HEIGHT - SQUARE_SIZE) // 2,
    SQUARE_SIZE,
    SQUARE_SIZE,
)

# 圆形物理系统初始化
circle_pos = pygame.Vector2(SCREEN_WIDTH // 2, 50)  # 从顶部开始下落
circle_velocity = pygame.Vector2(3, 0)  # 初始水平速度

while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 输入处理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square_pos.y = max(0, square_pos.y - MOVE_STEP)
    if keys[pygame.K_DOWN]:
        square_pos.y = min(SCREEN_HEIGHT - SQUARE_SIZE, square_pos.y + MOVE_STEP)
    if keys[pygame.K_LEFT]:
        square_pos.x = max(0, square_pos.x - MOVE_STEP)
    if keys[pygame.K_RIGHT]:
        square_pos.x = min(SCREEN_WIDTH - SQUARE_SIZE, square_pos.x + MOVE_STEP)

    # 圆形物理模拟
    # 应用重力
    circle_velocity.y = min(circle_velocity.y + GRAVITY, MAX_Y_SPEED)

    # 更新位置
    new_pos = circle_pos + circle_velocity

    # 边界碰撞检测
    # 底部碰撞
    if new_pos.y > SCREEN_HEIGHT - CIRCLE_RADIUS:
        new_pos.y = SCREEN_HEIGHT - CIRCLE_RADIUS
        circle_velocity.y *= -BOUNCE_STRENGTH
        circle_velocity.x *= DAMPING  # 水平方向能量衰减

    # 顶部碰撞
    if new_pos.y < CIRCLE_RADIUS:
        new_pos.y = CIRCLE_RADIUS
        circle_velocity.y *= -BOUNCE_STRENGTH

    # 右侧碰撞
    if new_pos.x > SCREEN_WIDTH - CIRCLE_RADIUS:
        new_pos.x = SCREEN_WIDTH - CIRCLE_RADIUS
        circle_velocity.x *= -BOUNCE_STRENGTH

    # 左侧碰撞
    if new_pos.x < CIRCLE_RADIUS:
        new_pos.x = CIRCLE_RADIUS
        circle_velocity.x *= -BOUNCE_STRENGTH

    # 应用最终位置
    circle_pos = new_pos

    # 能量衰减（防止无限弹跳）
    if abs(circle_velocity.x) < 0.1:
        circle_velocity.x = 0
    if abs(circle_velocity.y) < 0.1:
        circle_velocity.y = 0

    # 渲染
    screen.fill("black")
    pygame.draw.rect(screen, "red", square_pos)
    pygame.draw.circle(screen, "blue", circle_pos, CIRCLE_RADIUS)
    pygame.display.flip()
    clock.tick(60)
#====================================================
#可触碰版
import pygame
import math
import random

# 常量配置
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SQUARE_SIZE = 50
MOVE_STEP = 20
BALL_MOVE_FORCE = 0.5  # 小球控制力度

# 物理参数
CIRCLE_RADIUS = 20
GRAVITY = 0.7
DAMPING = 0.75  # 摩擦衰减
BOUNCE_STRENGTH = 0.9  # 增加弹跳强度
AIR_RESISTANCE = 0.99  # 空气阻力
MAX_Y_SPEED = 15  # 最大下落速度
SQUARE_MASS = 2.0  # 方块质量

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 游戏对象初始化
square = pygame.Rect(
    (SCREEN_WIDTH - SQUARE_SIZE) // 2,
    (SCREEN_HEIGHT - SQUARE_SIZE) // 2,
    SQUARE_SIZE,
    SQUARE_SIZE,
)
prev_square_pos = square.copy()

circle_pos = pygame.Vector2(SCREEN_WIDTH // 2, 50)
circle_vel = pygame.Vector2(3, 0)


def reset_ball():
    """重置小球位置和速度"""
    global circle_pos, circle_vel
    circle_pos = pygame.Vector2(SCREEN_WIDTH // 2, 50)
    # 随机方向（0-360度）初始速度
    angle = math.radians(random.uniform(0, 360))
    speed = 5
    circle_vel = pygame.Vector2(speed * math.cos(angle), speed * math.sin(angle))


def check_collision(rect, circle_pos, radius):
    """碰撞检测函数"""
    closest_x = max(rect.left, min(circle_pos.x, rect.right))
    closest_y = max(rect.top, min(circle_pos.y, rect.bottom))
    dx = circle_pos.x - closest_x
    dy = circle_pos.y - closest_y
    distance_sq = dx**2 + dy**2

    # 处理顶点碰撞
    is_corner = (closest_x in (rect.left, rect.right)) and (
        closest_y in (rect.top, rect.bottom)
    )

    if is_corner and distance_sq < radius**2:
        distance = math.sqrt(distance_sq)
        normal = (
            pygame.Vector2(dx / distance, dy / distance)
            if distance != 0
            else pygame.Vector2(0, 1)
        )
        return True, normal, radius - distance

    if distance_sq < radius**2:
        distance = math.sqrt(distance_sq)
        if distance == 0:
            left = circle_pos.x - rect.left
            right = rect.right - circle_pos.x
            top = circle_pos.y - rect.top
            bottom = rect.bottom - circle_pos.y
            min_side = min(left, right, top, bottom)
            if min_side == left:
                normal = pygame.Vector2(-1, 0)
            elif min_side == right:
                normal = pygame.Vector2(1, 0)
            elif min_side == top:
                normal = pygame.Vector2(0, -1)
            else:
                normal = pygame.Vector2(0, 1)
            return True, normal, radius
        normal = pygame.Vector2(dx / distance, dy / distance)
        return True, normal, radius - distance

    if rect.collidepoint(circle_pos):
        left = circle_pos.x - rect.left
        right = rect.right - circle_pos.x
        top = circle_pos.y - rect.top
        bottom = rect.bottom - circle_pos.y
        min_dist = min(left, right, top, bottom)
        if min_dist < radius:
            if min_dist == left:
                normal = pygame.Vector2(-1, 0)
            elif min_dist == right:
                normal = pygame.Vector2(1, 0)
            elif min_dist == top:
                normal = pygame.Vector2(0, -1)
            else:
                normal = pygame.Vector2(0, 1)
            return True, normal, radius - min_dist

    return False, None, 0


def handle_boundary_collision(pos, vel, radius):
    """边界碰撞处理"""
    # 垂直碰撞（增加底部弹跳强度）
    if pos.y > SCREEN_HEIGHT - radius:
        pos.y = SCREEN_HEIGHT - radius
        vel.y *= -BOUNCE_STRENGTH * 1.2  # 增加底部弹跳力度
        vel.x *= DAMPING
    elif pos.y < radius:
        pos.y = radius
        vel.y *= -BOUNCE_STRENGTH

    # 水平碰撞
    if pos.x > SCREEN_WIDTH - radius:
        pos.x = SCREEN_WIDTH - radius
        vel.x *= -BOUNCE_STRENGTH
    elif pos.x < radius:
        pos.x = radius
        vel.x *= -BOUNCE_STRENGTH

    return pos, vel


# 主循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Q键重置小球
                reset_ball()

    # 方块控制
    keys = pygame.key.get_pressed()
    prev_square_pos = square.copy()
    if keys[pygame.K_UP]:
        square.y = max(0, square.y - MOVE_STEP)
    if keys[pygame.K_DOWN]:
        square.y = min(SCREEN_HEIGHT - SQUARE_SIZE, square.y + MOVE_STEP)
    if keys[pygame.K_LEFT]:
        square.x = max(0, square.x - MOVE_STEP)
    if keys[pygame.K_RIGHT]:
        square.x = min(SCREEN_WIDTH - SQUARE_SIZE, square.x + MOVE_STEP)

    # 小球WASD控制
    if keys[pygame.K_w]:
        circle_vel.y -= BALL_MOVE_FORCE
    if keys[pygame.K_s]:
        circle_vel.y += BALL_MOVE_FORCE
    if keys[pygame.K_a]:
        circle_vel.x -= BALL_MOVE_FORCE
    if keys[pygame.K_d]:
        circle_vel.x += BALL_MOVE_FORCE

    # 计算方块速度
    square_vel = pygame.Vector2(
        square.x - prev_square_pos.x, square.y - prev_square_pos.y
    )

    # 小球物理模拟
    circle_vel.y = min(circle_vel.y + GRAVITY, MAX_Y_SPEED)
    circle_vel *= AIR_RESISTANCE

    # 预测新位置
    new_pos = circle_pos + circle_vel

    # 边界碰撞处理
    new_pos, circle_vel = handle_boundary_collision(new_pos, circle_vel, CIRCLE_RADIUS)

    # 方块碰撞处理
    collided, normal, penetration = check_collision(square, new_pos, CIRCLE_RADIUS)
    if collided:
        new_pos += normal * penetration
        vel_normal = circle_vel.dot(normal) * normal
        vel_tangent = circle_vel - vel_normal

        # 加入方块速度影响
        square_effect = square_vel.dot(normal) * (1 / SQUARE_MASS)

        circle_vel = (
            (-vel_normal * BOUNCE_STRENGTH)
            + vel_tangent * DAMPING
            + square_effect * normal * 2
        )

    # 更新位置
    circle_pos = new_pos

    # 速度衰减
    if circle_vel.magnitude() < 0.1:
        circle_vel = pygame.Vector2()

    # 渲染
    screen.fill("black")
    pygame.draw.rect(screen, "red", square)
    pygame.draw.circle(screen, "blue", circle_pos, CIRCLE_RADIUS)
    pygame.display.flip()
    clock.tick(60)




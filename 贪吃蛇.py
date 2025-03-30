import random
import pygame

# 初始化 Pygame
pygame.init()

# 定义颜色
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# 设置游戏窗口尺寸
dis_width = 600
dis_height = 400

# 创建游戏窗口
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("贪吃蛇游戏-多食物加速版")

# 设置时钟
clock = pygame.time.Clock()

# 定义蛇的大小和速度
snake_block = 10
initial_speed = 10
max_speed = 30

# 设置字体
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("得分: " + str(score), True, black)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def generate_food_position(snake_list, width, height, block_size, existing_foods=[]):
    """生成不在蛇身上且不与其他食物重叠的坐标"""
    while True:
        foodx = round(random.randrange(0, width - block_size) / 10.0) * 10.0
        foody = round(random.randrange(0, height - block_size) / 10.0) * 10.0
        if [foodx, foody] not in snake_list and (foodx, foody) not in existing_foods:
            return foodx, foody


def gameLoop():
    while True:  # 外层循环支持多次重开
        game_over = False
        game_close = False
        current_speed = initial_speed  # 当前速度
        speed_counter = 0  # 加速计数器
        food_count = 3  # 同时存在的食物数量

        # 初始化游戏状态
        x1 = dis_width / 2
        y1 = dis_height / 2
        x1_change = 0
        y1_change = 0
        snake_List = []
        Length_of_snake = 1

        # 初始化食物
        foods = []
        for _ in range(food_count):
            new_food = generate_food_position(
                snake_List, dis_width, dis_height, snake_block, foods
            )
            foods.append(new_food)

        while not game_over:
            # 游戏结束处理循环
            while game_close:
                dis.fill(blue)
                message(f"你输了! 得分: {Length_of_snake-1} 按 Q 退出或按 C 再玩", red)
                pygame.display.update()
                clock.tick(initial_speed)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            pygame.quit()
                            return
                        if event.key == pygame.K_c:
                            game_close = False
                            game_over = True

            # 事件处理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN:
                    # 防止反向移动
                    if event.key == pygame.K_LEFT and x1_change == 0:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT and x1_change == 0:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP and y1_change == 0:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN and y1_change == 0:
                        y1_change = snake_block
                        x1_change = 0

            # 移动蛇头
            x1 += x1_change
            y1 += y1_change

            # 边界碰撞检测
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True

            # 渲染画面
            dis.fill(blue)

            # 绘制所有食物
            for fx, fy in foods:
                pygame.draw.rect(dis, green, [fx, fy, snake_block, snake_block])

            # 更新蛇身
            snake_Head = [x1, y1]
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]

            # 自碰撞检测
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True

            our_snake(snake_block, snake_List)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            # 进食检测
            eaten_index = None
            for idx, (fx, fy) in enumerate(foods):
                if x1 == fx and y1 == fy:
                    eaten_index = idx
                    Length_of_snake += 1
                    speed_counter += 1

                    # 加速逻辑：每吃2个食物加速一次
                    if speed_counter >= 2:
                        current_speed = min(max_speed, current_speed + 2)
                        speed_counter = 0
                    break

            # 更新食物列表
            if eaten_index is not None:
                del foods[eaten_index]
                new_food = generate_food_position(
                    snake_List, dis_width, dis_height, snake_block, foods
                )
                foods.append(new_food)

            clock.tick(current_speed)


gameLoop()

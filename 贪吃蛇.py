"""
终极贪吃蛇 - 优化版
功能特性：
1. 多食物系统（最多20个）
2. 动态障碍物系统（每40秒刷新位置）
3. 自适应难度（吃食物加速）
4. 碰撞安全距离保护
5. 高分存档功能
6. 优化渲染性能
"""

import random
import math
import pygame
import json
from pathlib import Path

# 初始化Pygame引擎
pygame.init()

# 游戏配置常量
class Config:
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 900
    SNAKE_SIZE = 10
    INIT_SPEED = 10
    MAX_SPEED = 30
    MIN_OBSTACLE_DIST = 150  # 障碍物与玩家的最小距离
    INIT_FOOD_NUM = 20       # 初始食物数量
    MAX_OBSTACLES = 10       # 最大障碍物数量
    OBSTACLE_REFRESH = 40000 # 障碍物刷新间隔(ms)
    SAVE_FILE = "highscore.json"

    # 颜色配置
    COLORS = {
        "bg": (50, 153, 213),    # 背景蓝
        "snake": (0, 0, 0),      # 黑色蛇身
        "food": (0, 255, 0),     # 绿色食物
        "obstacle": (0, 0, 0),   # 黑色障碍物
        "text": (255, 255, 255), # 白色文字
        "warning": (213, 50, 80) # 红色警告
    }

class GameAssets:
    """游戏资源管理类"""
    def __init__(self):
        self.fonts = {
            'normal': self.load_font(None, 25),
            'bold': self.load_font(None, 35, bold=True)
        }

    @staticmethod
    def load_font(name, size, bold=False):
        """安全加载字体"""
        try:
            return pygame.font.SysFont(name, size, bold=bold)
        except Exception as e:
            print(f"字体加载失败: {e}, 使用默认字体")
            return pygame.font.Font(None, size)

class GameState:
    """游戏状态管理类"""
    def __init__(self):
        self.snake = []
        self.foods = []
        self.obstacles = []
        self.speed = Config.INIT_SPEED
        self.score = 0
        self.high_score = self.load_highscore()
        self.last_obstacle_refresh = pygame.time.get_ticks()

    @staticmethod
    def load_highscore():
        """加载历史最高分"""
        save_path = Path(Config.SAVE_FILE)
        if save_path.exists():
            try:
                with open(save_path, 'r') as f:
                    return json.load(f).get('high_score', 0)
            except:
                return 0
        return 0

    def save_highscore(self):
        """保存最高分"""
        if self.score > self.high_score:
            with open(Config.SAVE_FILE, 'w') as f:
                json.dump({'high_score': self.score}, f)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
        pygame.display.set_caption("终极贪吃蛇-优化版")

        self.assets = GameAssets()
        self.clock = pygame.time.Clock()
        self.state = GameState()
        self.direction = (0, 0)
        self.running = True
        self.show_help = True

        # 初始化游戏元素
        self.init_game()

    def init_game(self):
        """初始化游戏状态"""
        player_pos = (Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2)

        # 生成初始元素
        self.state.foods = self.generate_positions(
            Config.INIT_FOOD_NUM,
            avoid=[player_pos],
            min_dist=50
        )
        self.state.obstacles = self.generate_positions(
            Config.MAX_OBSTACLES,
            avoid=self.state.foods + [player_pos],
            min_dist=Config.MIN_OBSTACLE_DIST
        )

        # 重置蛇状态
        self.state.snake = [player_pos]
        self.direction = (0, 0)
        self.state.speed = Config.INIT_SPEED
        self.state.score = 0

    def generate_positions(self, count, avoid=None, min_dist=0):
        """生成安全位置的高级算法"""
        positions = []
        avoid = avoid or []
        attempts = 0

        while len(positions) < count and attempts < 1000:
            new_pos = (
                round(random.randrange(0, Config.SCREEN_WIDTH - Config.SNAKE_SIZE) / 10.0) * 10.0,
                round(random.randrange(0, Config.SCREEN_HEIGHT - Config.SNAKE_SIZE) / 10.0) * 10.0
            )

            # 碰撞检测优化
            collision = (
                new_pos in avoid or
                new_pos in positions or
                any(math.hypot(new_pos[0]-p[0], new_pos[1]-p[1]) < min_dist for p in avoid)
            )

            if not collision:
                positions.append(new_pos)
            attempts += 1

        return positions

    def handle_input(self):
        """处理用户输入"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type == pygame.KEYDOWN:
                # 方向控制
                new_dir = None
                if event.key == pygame.K_LEFT and self.direction[0] == 0:
                    new_dir = (-Config.SNAKE_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.direction[0] == 0:
                    new_dir = (Config.SNAKE_SIZE, 0)
                elif event.key == pygame.K_UP and self.direction[1] == 0:
                    new_dir = (0, -Config.SNAKE_SIZE)
                elif event.key == pygame.K_DOWN and self.direction[1] == 0:
                    new_dir = (0, Config.SNAKE_SIZE)

                if new_dir:
                    self.direction = new_dir

    def update_game(self):
        """更新游戏状态"""
        # 移动蛇头
        head_x = self.state.snake[-1][0] + self.direction[0]
        head_y = self.state.snake[-1][1] + self.direction[1]
        new_head = (head_x, head_y)

        # 碰撞检测
        if self.check_collision(new_head):
            self.game_over()
            return

        # 更新蛇身
        self.state.snake.append(new_head)

        # 进食检测
        if new_head in self.state.foods:
            self.state.foods.remove(new_head)
            self.state.score += 1
            self.update_difficulty()
            # 补充新食物
            new_foods = self.generate_positions(1, avoid=self.state.snake + self.state.obstacles)
            self.state.foods.extend(new_foods)
        else:
            # 保持蛇长
            self.state.snake.pop(0)

        # 障碍物刷新
        if pygame.time.get_ticks() - self.state.last_obstacle_refresh > Config.OBSTACLE_REFRESH:
            self.state.obstacles = self.generate_positions(
                Config.MAX_OBSTACLES,
                avoid=self.state.snake + self.state.foods,
                min_dist=Config.MIN_OBSTACLE_DIST
            )
            self.state.last_obstacle_refresh = pygame.time.get_ticks()

    def check_collision(self, position):
        """高级碰撞检测"""
        # 边界检测
        if (position[0] < 0 or position[0] >= Config.SCREEN_WIDTH or
            position[1] < 0 or position[1] >= Config.SCREEN_HEIGHT):
            return True

        # 自碰撞和障碍物检测
        return (position in self.state.snake[:-1] or
                position in self.state.obstacles)

    def update_difficulty(self):
        """动态难度调整"""
        if self.state.score % 2 == 0:
            self.state.speed = min(Config.MAX_SPEED, self.state.speed + 1)

    def draw_ui(self):
        """绘制游戏界面"""
        # 背景
        self.screen.fill(Config.COLORS["bg"])

        # 绘制食物
        for food in self.state.foods:
            pygame.draw.rect(self.screen, Config.COLORS["food"],
                           [food[0], food[1], Config.SNAKE_SIZE, Config.SNAKE_SIZE])

        # 绘制障碍物
        for obs in self.state.obstacles:
            pygame.draw.rect(self.screen, Config.COLORS["obstacle"],
                           [obs[0], obs[1], Config.SNAKE_SIZE, Config.SNAKE_SIZE])

        # 绘制蛇
        for seg in self.state.snake:
            pygame.draw.rect(self.screen, Config.COLORS["snake"],
                           [seg[0], seg[1], Config.SNAKE_SIZE, Config.SNAKE_SIZE])

        # 显示分数
        score_text = self.assets.fonts['bold'].render(
            f"得分: {self.state.score}  最高分: {self.state.high_score}",
            True, Config.COLORS["text"])
        self.screen.blit(score_text, (10, 10))

    def show_message(self, text, color, y_offset=0, font_size=35):
        """居中显示文本"""
        font = self.assets.fonts['bold'] if font_size > 30 else self.assets.fonts['normal']
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(
            center=(Config.SCREEN_WIDTH//2, Config.SCREEN_HEIGHT//2 + y_offset))
        self.screen.blit(text_surface, text_rect)

    def game_over(self):
        """游戏结束处理"""
        self.state.save_highscore()

        # 显示结束画面
        self.screen.fill(Config.COLORS["bg"])
        self.show_message("游戏结束!", Config.COLORS["warning"], -40, 45)
        self.show_message(f"最终得分: {self.state.score}", Config.COLORS["text"], 0)
        self.show_message("按R重玩  Q退出", Config.COLORS["text"], 40)
        pygame.display.update()

        # 处理结束选项
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    self.init_game()
                    return

    def run(self):
        """主游戏循环"""
        while self.running:
            self.handle_input()

            if self.show_help:
                # 显示帮助界面
                self.screen.fill(Config.COLORS["bg"])
                self.show_message("准备开始!", Config.COLORS["warning"], -40, 45)
                self.show_message("方向键控制移动", Config.COLORS["text"], 0)
                self.show_message("按任意键开始", Config.COLORS["text"], 40)
                pygame.display.update()

                # 等待开始输入
                wait = True
                while wait:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            wait = False
                            self.show_help = False
                        if event.type == pygame.QUIT:
                            self.running = False
                            return

            else:
                # 正常游戏流程
                self.update_game()
                self.draw_ui()
                pygame.display.update()
                self.clock.tick(self.state.speed)

        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

# ============================================================================
# 画画版
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()


gameLoop()

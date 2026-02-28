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

# 尝试导入pywin32模块用于控制输入法
try:
    import win32api
    import win32con
    import win32gui
    import win32clipboard
    HAVE_WIN32 = True
except ImportError:
    HAVE_WIN32 = False

# 使用ctypes直接调用Windows API
import ctypes
user32 = ctypes.windll.user32
imm32 = ctypes.windll.imm32

# 输入法相关常量
WM_INPUTLANGCHANGEREQUEST = 0x0050
INPUTLANGCHANGE_SYSCHARSET = 0x0001

# 英文输入法的LOCALE_ID
ENGLISH_LOCALE = 0x04090409

# 输入法状态常量
IME_CMODE_ALPHANUMERIC = 0x0000
IME_CMODE_NATIVE = 0x0001
IME_CMODE_FULLSHAPE = 0x0008
IME_CMODE_ROMAN = 0x0010

# 初始化Pygame引擎
pygame.init()

# 游戏配置常量
class Config:
    SCREEN_WIDTH = 1500
    SCREEN_HEIGHT = 900
    SNAKE_SIZE = 10
    INIT_SPEED = 8
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
        # 尝试使用支持中文的系统字体
        chinese_fonts = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS', 'WenQuanYi Micro Hei']
        
        for font_name in chinese_fonts:
            try:
                return pygame.font.SysFont(font_name, size, bold=bold)
            except:
                continue
        
        # 如果所有中文字体都失败，尝试默认字体
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
        self.snake_colors = []  # 存储蛇的渐变色
        self.current_head_color = Config.COLORS["snake"]  # 当前头部颜色
        self.last_color_change_score = 0  # 上次颜色变化时的分数
        self.collection_range = Config.SNAKE_SIZE
        self.food_collection_animations = []
        self.food_attraction_animations = []

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
        pygame.display.set_caption("炫彩贪吃蛇")

        self.assets = GameAssets()
        self.clock = pygame.time.Clock()
        self.state = GameState()
        self.direction = (0, 0)
        self.running = True
        self.show_help = True
        self.food_alpha = 255
        self.food_alpha_dir = -5
        self.original_input_locale = None
        self.window_handle = None
        # 初始化颜色参数
        self.last_head_color = Config.COLORS["snake"]
        self.last_tail_color = Config.COLORS["snake"]

        # 保存原始输入法
        self.save_original_input()

        # 初始化游戏元素
        self.init_game()
        
        # 获取Pygame窗口句柄
        self.get_window_handle()
    
    def save_original_input(self):
        """保存原始输入法"""
        try:
            # 使用win32api获取当前输入法，更可靠
            hwnd = win32gui.GetForegroundWindow()
            thread_id = win32api.GetWindowThreadProcessId(hwnd)[0]
            self.original_input_locale = win32api.GetKeyboardLayout(thread_id)
        except Exception:
            pass
    
    def get_window_handle(self):
        """获取Pygame窗口句柄"""
        if HAVE_WIN32:
            try:
                # 获取当前窗口标题
                title = pygame.display.get_caption()[0]
                
                # 枚举所有窗口查找Pygame窗口
                def enum_windows_callback(hwnd, extra):
                    window_title = win32gui.GetWindowText(hwnd)
                    if title in window_title:
                        extra.append(hwnd)
                        return False  # 停止枚举
                    return True
                
                windows = []
                win32gui.EnumWindows(enum_windows_callback, windows)
                
                if windows:
                    self.window_handle = windows[0]
                else:
                    # 尝试获取前景窗口
                    self.window_handle = win32gui.GetForegroundWindow()
                    
            except Exception:
                pass
    
    def switch_to_english_input(self):
        """切换到英文输入法"""
        try:
            hwnd = user32.GetForegroundWindow()
            # 使用ImmSetConversionStatus强制切换到英文模式
            hIMC = imm32.ImmGetContext(hwnd)
            if hIMC:
                imm32.ImmSetConversionStatus(hIMC, IME_CMODE_ALPHANUMERIC, 0)
                imm32.ImmReleaseContext(hwnd, hIMC)
            # 模拟Ctrl+空格键切换
            user32.keybd_event(0x11, 0, 0, 0)  # 按下Ctrl键
            user32.keybd_event(0x20, 0, 0, 0)  # 按下空格键
            user32.keybd_event(0x20, 0, 2, 0)  # 释放空格键
            user32.keybd_event(0x11, 0, 2, 0)  # 释放Ctrl键
        except Exception:
            pass
    
    def restore_original_input(self):
        """恢复原始输入法"""
        if self.original_input_locale:
            try:
                # 使用win32api恢复输入法，更可靠
                hwnd = win32gui.GetForegroundWindow()
                thread_id = win32api.GetWindowThreadProcessId(hwnd)[0]
                # 使用KLF_ACTIVATE标志确保激活输入法
                win32api.ActivateKeyboardLayout(self.original_input_locale, win32con.KLF_ACTIVATE)
            except Exception:
                pass

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
        # 重置颜色参数
        self.last_head_color = Config.COLORS["snake"]
        self.last_tail_color = Config.COLORS["snake"]
        # 初始化蛇的渐变色列表
        self.state.snake_colors = [Config.COLORS["snake"]]
        self.state.current_head_color = Config.COLORS["snake"]  # 重置当前头部颜色
        self.state.last_color_change_score = 0  # 重置上次颜色变化分数
        self.state.collection_range = Config.SNAKE_SIZE
        self.state.food_collection_animations = []
        self.state.food_attraction_animations = []

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
                # 方向控制（使用事件处理，响应更及时）
                if event.key == pygame.K_LEFT and self.direction[0] == 0:
                    self.direction = (-Config.SNAKE_SIZE, 0)
                elif event.key == pygame.K_RIGHT and self.direction[0] == 0:
                    self.direction = (Config.SNAKE_SIZE, 0)
                elif event.key == pygame.K_UP and self.direction[1] == 0:
                    self.direction = (0, -Config.SNAKE_SIZE)
                elif event.key == pygame.K_DOWN and self.direction[1] == 0:
                    self.direction = (0, Config.SNAKE_SIZE)

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

        # 进食检测和食物吸引
        food_eaten = False
        
        # 处理食物吸引动画
        # 直接遍历并移除动画，避免索引问题
        remaining_animations = []
        
        for anim in self.state.food_attraction_animations:
            # 计算移动方向
            dx = new_head[0] - anim['position'][0]
            dy = new_head[1] - anim['position'][1]
            distance = math.hypot(dx, dy)
            
            if distance > 0:
                # 向蛇头移动，使用非常快的速度
                speed = 30  # 最大速度
                anim['position'] = (
                    anim['position'][0] + dx/distance * speed,
                    anim['position'][1] + dy/distance * speed
                )
            
            # 重新计算移动后的距离
            new_distance = math.hypot(new_head[0] - anim['position'][0], new_head[1] - anim['position'][1])
            
            # 检查是否到达蛇头
            if new_distance <= 15:
                # 直接处理食物收集
                self.state.score += 1
                food_eaten = True
                
                # 每增加2分改变蛇的颜色（渐变色效果）
                if self.state.score > 0 and self.state.score % 2 == 0 and self.state.score != self.state.last_color_change_score:
                    # 生成新的头部颜色和尾部颜色
                    new_head_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    new_tail_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    # 保存颜色参数供后续使用
                    self.last_head_color = new_head_color
                    self.last_tail_color = new_tail_color
                    self.state.current_head_color = new_head_color
                    self.state.last_color_change_score = self.state.score
                    # 生成新的渐变色
                    self.state.snake_colors = []
                    if len(self.state.snake) > 1:
                        for i in range(len(self.state.snake)):
                            # 计算颜色过渡（反转渐变方向，确保头部是头部颜色，尾巴是尾部颜色）
                            ratio = i / (len(self.state.snake) - 1)
                            r = int(new_tail_color[0] * (1 - ratio) + new_head_color[0] * ratio)
                            g = int(new_tail_color[1] * (1 - ratio) + new_head_color[1] * ratio)
                            b = int(new_tail_color[2] * (1 - ratio) + new_head_color[2] * ratio)
                            self.state.snake_colors.append((r, g, b))
                    else:
                        # 蛇身只有一节时，直接使用头部颜色
                        self.state.snake_colors = [new_head_color]
                
                # 每增加5分扩大收集范围（每次增加5像素）
                if self.state.score > 0 and self.state.score % 5 == 0:
                    self.state.collection_range += 5
                
                # 添加食物收集动画
                self.state.food_collection_animations.append({
                    'position': new_head,
                    'size': Config.SNAKE_SIZE,
                    'alpha': 255
                })
                # 动画到达蛇头，不添加到剩余列表
            else:
                # 动画未到达蛇头，保留
                remaining_animations.append(anim)

        # 更新动画列表，只保留未到达蛇头的动画
        self.state.food_attraction_animations = remaining_animations

        # 补充新食物
        if food_eaten:
            self.update_difficulty()
            new_foods = self.generate_positions(1, avoid=self.state.snake + self.state.obstacles)
            self.state.foods.extend(new_foods)

        # 检测食物是否进入收集范围
        foods_to_remove = []
        for food in self.state.foods:
            # 使用收集范围检测食物
            distance = math.hypot(new_head[0] - food[0], new_head[1] - food[1])
            
            if distance <= 1:
                # 已经在1像素范围内，直接收集
                self.state.score += 1
                food_eaten = True
                
                # 每增加2分改变蛇的颜色（渐变色效果）
                if self.state.score > 0 and self.state.score % 2 == 0 and self.state.score != self.state.last_color_change_score:
                    # 生成新的头部颜色和尾部颜色
                    new_head_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    new_tail_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    # 保存颜色参数供后续使用
                    self.last_head_color = new_head_color
                    self.last_tail_color = new_tail_color
                    self.state.current_head_color = new_head_color
                    self.state.last_color_change_score = self.state.score
                    # 生成新的渐变色
                    self.state.snake_colors = []
                    if len(self.state.snake) > 1:
                        for i in range(len(self.state.snake)):
                            # 计算颜色过渡（反转渐变方向，确保头部是头部颜色，尾巴是尾部颜色）
                            ratio = i / (len(self.state.snake) - 1)
                            r = int(new_tail_color[0] * (1 - ratio) + new_head_color[0] * ratio)
                            g = int(new_tail_color[1] * (1 - ratio) + new_head_color[1] * ratio)
                            b = int(new_tail_color[2] * (1 - ratio) + new_head_color[2] * ratio)
                            self.state.snake_colors.append((r, g, b))
                    else:
                        # 蛇身只有一节时，直接使用头部颜色
                        self.state.snake_colors = [new_head_color]
                
                # 每增加5分扩大收集范围（每次增加5像素）
                if self.state.score > 0 and self.state.score % 5 == 0:
                    self.state.collection_range += 5
                
                # 添加食物收集动画
                self.state.food_collection_animations.append({
                    'position': food,
                    'size': Config.SNAKE_SIZE,
                    'alpha': 255
                })
                
                foods_to_remove.append(food)
            elif distance <= self.state.collection_range:
                # 在收集范围内但不在1像素范围内，添加吸引动画
                # 检查是否已经有该食物的动画
                has_anim = any(anim['original_position'] == food for anim in self.state.food_attraction_animations)
                if not has_anim:
                    self.state.food_attraction_animations.append({
                        'position': food,
                        'original_position': food,
                        'size': Config.SNAKE_SIZE
                    })
                    foods_to_remove.append(food)

        # 移除被处理的食物
        for food in foods_to_remove:
            if food in self.state.foods:
                self.state.foods.remove(food)

        # 补充新食物
        if food_eaten:
            self.update_difficulty()
            new_foods = self.generate_positions(1, avoid=self.state.snake + self.state.obstacles)
            self.state.foods.extend(new_foods)

        # 保持蛇长（只有在没有吃到食物时才减少尾巴）
        if not food_eaten:
            self.state.snake.pop(0)
        else:
            # 吃到食物时，蛇身增加一节
            pass
        
        # 重新计算渐变颜色，确保颜色列表与蛇身长度一致
        if len(self.state.snake) > 1 and hasattr(self, 'last_head_color') and hasattr(self, 'last_tail_color'):
            # 使用上一次的颜色参数重新计算渐变
            new_head_color = self.last_head_color
            new_tail_color = self.last_tail_color
            self.state.snake_colors = []
            for i in range(len(self.state.snake)):
                # 计算颜色过渡（反转渐变方向，确保头部是头部颜色，尾巴是尾部颜色）
                ratio = i / (len(self.state.snake) - 1)
                r = int(new_tail_color[0] * (1 - ratio) + new_head_color[0] * ratio)
                g = int(new_tail_color[1] * (1 - ratio) + new_head_color[1] * ratio)
                b = int(new_tail_color[2] * (1 - ratio) + new_head_color[2] * ratio)
                self.state.snake_colors.append((r, g, b))
        else:
            # 初始化颜色列表
            if not self.state.snake_colors:
                self.state.snake_colors = [Config.COLORS["snake"]] * len(self.state.snake)

        # 更新食物收集动画
        for anim in self.state.food_collection_animations[:]:
            anim['size'] += 1
            anim['alpha'] -= 15  # 加快动画速度，减少卡顿
            if anim['alpha'] <= 0:
                self.state.food_collection_animations.remove(anim)

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
        # 每2分加速一次，而不是每次吃到食物都加速
        if self.state.score > 0 and self.state.score % 2 == 0:
            self.state.speed = min(Config.MAX_SPEED, self.state.speed + 1)

    def draw_ui(self):
        """绘制游戏界面"""
        # 背景
        self.screen.fill(Config.COLORS["bg"])

        # 绘制食物（带发光和闪烁效果）
        self.food_alpha += self.food_alpha_dir
        if self.food_alpha <= 150 or self.food_alpha >= 255:
            self.food_alpha_dir *= -1
        
        # 绘制发光效果
        glow_surface = pygame.Surface((Config.SNAKE_SIZE * 3, Config.SNAKE_SIZE * 3), pygame.SRCALPHA)
        glow_color = (0, 255, 100, 50)
        pygame.draw.ellipse(glow_surface, glow_color, glow_surface.get_rect())
        
        # 绘制食物本身
        food_surface = pygame.Surface((Config.SNAKE_SIZE, Config.SNAKE_SIZE), pygame.SRCALPHA)
        food_color = Config.COLORS["food"] + (self.food_alpha,)
        food_surface.fill(food_color)
        
        # 绘制普通食物
        for food in self.state.foods:
            # 绘制发光效果
            glow_pos = (food[0] - Config.SNAKE_SIZE, food[1] - Config.SNAKE_SIZE)
            self.screen.blit(glow_surface, glow_pos)
            # 绘制食物
            self.screen.blit(food_surface, (food[0], food[1]))
        
        # 绘制食物吸引动画
        for anim in self.state.food_attraction_animations:
            # 绘制发光效果
            glow_pos = (anim['position'][0] - Config.SNAKE_SIZE, anim['position'][1] - Config.SNAKE_SIZE)
            self.screen.blit(glow_surface, glow_pos)
            # 绘制食物
            self.screen.blit(food_surface, (anim['position'][0], anim['position'][1]))

        # 绘制障碍物
        for obs in self.state.obstacles:
            pygame.draw.rect(self.screen, Config.COLORS["obstacle"],
                           [obs[0], obs[1], Config.SNAKE_SIZE, Config.SNAKE_SIZE])

        # 绘制蛇（使用渐变色）
        for i, seg in enumerate(self.state.snake):
            # 确保颜色列表与蛇身长度一致
            if i < len(self.state.snake_colors):
                color = self.state.snake_colors[i]
            else:
                color = (0, 0, 0)  # 默认黑色
            pygame.draw.rect(self.screen, color,
                           [seg[0], seg[1], Config.SNAKE_SIZE, Config.SNAKE_SIZE])
        
        # 绘制食物收集动画
        for anim in self.state.food_collection_animations:
            if anim['alpha'] > 0:
                anim_surface = pygame.Surface((anim['size'], anim['size']), pygame.SRCALPHA)
                anim_color = (0, 255, 100, anim['alpha'])
                pygame.draw.ellipse(anim_surface, anim_color, anim_surface.get_rect())
                pos = (anim['position'][0] + Config.SNAKE_SIZE/2 - anim['size']/2,
                       anim['position'][1] + Config.SNAKE_SIZE/2 - anim['size']/2)
                self.screen.blit(anim_surface, pos)

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

        # 确保游戏结束界面时使用英文输入法（只切换一次）
        self.switch_to_english_input()

        # 处理结束选项
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (
                    event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                    self.running = False
                    # 恢复原始输入法
                    self.restore_original_input()
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    # 重玩时不需要切换输入法
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
                            # 退出时恢复输入法
                            self.restore_original_input()
                            return

            else:
                # 正常游戏流程（不再频繁切换输入法）
                self.update_game()
                self.draw_ui()
                pygame.display.update()
                self.clock.tick(self.state.speed)

        # 恢复原始输入法
        self.restore_original_input()
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run()

# ============================================================================
# 画画版 (暂时注释掉以测试Pygame版本)
'''
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
'''

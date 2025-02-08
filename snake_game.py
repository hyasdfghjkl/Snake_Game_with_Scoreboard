# -*- coding: utf-8 -*-
import pygame
import random
import sys

# 初始化pygame（必须的步骤，用于初始化所有pygame模块）
pygame.init()

# === 游戏常量配置 ===
WINDOW_WIDTH = 800  # 游戏窗口宽度（单位：像素）
WINDOW_HEIGHT = 600  # 游戏窗口高度（单位：像素）
CELL_SIZE = 20  # 网格单元格大小（单位：像素）
BASE_FPS = 5  # 基础游戏帧率（控制蛇的正常移动速度）
ACCELERATE_FPS = 14  # 加速时的游戏帧率

# 颜色定义（RGB格式）
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (255, 0, 0),
    "GREEN": (0, 255, 0),
    "BLUE": (0, 100, 200),
    "GRID": (40, 40, 40),  # 网格线颜色
    "SNAKE_HEAD": (0, 255, 0),  # 蛇头颜色
    "SNAKE_BODY": (0, 200, 0)  # 蛇身颜色
}

# === 游戏状态初始化 ===
snake = []  # 用列表存储蛇身体的坐标（每个元素是一个元组）
current_dir = (1, 0)  # 当前移动方向（使用向量表示，初始向右）
food_pos = (0, 0)  # 食物位置坐标
is_playing = True  # 游戏是否进行中的状态
score = 0  # 当前游戏分数
high_score = 0  # 历史最高分记录

# 初始化游戏窗口
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("贪吃蛇大作战")  # 窗口标题


def draw_grid():
    """绘制网格线背景，帮助玩家更好地观察位置"""
    # 绘制垂直网格线
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, COLORS["GRID"], (x, 0), (x, WINDOW_HEIGHT))
    # 绘制水平网格线
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, COLORS["GRID"], (0, y), (WINDOW_WIDTH, y))


def generate_food():
    """生成食物坐标，确保不在蛇身体上"""
    while True:
        # 计算网格坐标（确保在窗口范围内）
        x = random.randint(0, (WINDOW_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        y = random.randint(0, (WINDOW_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
        # 检查生成位置是否与蛇身体重叠
        if (x, y) not in snake:
            return (x, y)


def reset_game():
    """重置游戏所有状态到初始值"""
    global snake, current_dir, food_pos, is_playing, score
    snake = [(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)]  # 蛇初始位置在窗口中心
    current_dir = (1, 0)  # 初始方向向右
    food_pos = generate_food()  # 生成第一个食物
    is_playing = True  # 游戏状态设置为进行中
    score = 0  # 重置当前分数


def show_text(content, size, color, position):
    """在指定位置显示文字的工具函数"""
    font = pygame.font.SysFont('simhei', size)  # 使用黑体字
    text_surface = font.render(content, True, color)
    screen.blit(text_surface, position)


def load_highscore():
    """从文件读取历史最高分"""
    try:
        with open('highscore.txt', 'r') as f:
            return int(f.read())
    except FileNotFoundError:
        return 0  # 文件不存在时返回0分


def save_highscore():
    """保存最高分到文件"""
    with open('highscore.txt', 'w') as f:
        f.write(str(high_score))


# 初始化游戏
high_score = load_highscore()
reset_game()

# === 主游戏循环 ===
while True:
    # 处理事件队列（包括按键、窗口关闭等）
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 点击窗口关闭按钮
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Q键退出
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_r and not is_playing:  # R键重启游戏
                reset_game()
            # 方向键控制（已解决反向问题）
            if is_playing:
                new_dir = current_dir  # 默认保持当前方向
                if event.key == pygame.K_UP:
                    new_dir = (0, -1)
                elif event.key == pygame.K_DOWN:
                    new_dir = (0, 1)
                elif event.key == pygame.K_LEFT:
                    new_dir = (-1, 0)
                elif event.key == pygame.K_RIGHT:
                    new_dir = (1, 0)
                # 禁止直接反向（只有当新方向不相反时更新）
                if (current_dir[0] + new_dir[0] != 0) or (current_dir[1] + new_dir[1] != 0):
                    current_dir = new_dir

    # 获取当前按键状态实现加速功能
    keys = pygame.key.get_pressed()
    # 检查是否有方向键被按住（使用位运算优化判断）
    accelerate = any(keys[k] for k in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT))

    # 游戏进行中的逻辑处理
    if is_playing:
        # 计算新蛇头位置
        head_x, head_y = snake[0]
        dir_x, dir_y = current_dir
        new_head = (head_x + dir_x * CELL_SIZE, head_y + dir_y * CELL_SIZE)

        # 碰撞检测（边界和自身）
        if (new_head in snake or
                new_head[0] < 0 or
                new_head[0] >= WINDOW_WIDTH or
                new_head[1] < 0 or
                new_head[1] >= WINDOW_HEIGHT):
            is_playing = False
            # 更新最高分记录
            if score > high_score:
                high_score = score
                save_highscore()

        # 更新蛇的位置
        snake.insert(0, new_head)
        if new_head == food_pos:  # 吃到食物
            score += 10
            food_pos = generate_food()
        else:  # 没吃到食物时移除尾部
            snake.pop()

    # === 绘制游戏画面 ===
    screen.fill(COLORS["BLACK"])  # 填充背景色
    draw_grid()  # 绘制网格线

    # 绘制蛇的身体（使用渐变颜色）
    for i, (x, y) in enumerate(snake):
        # 根据部位设置颜色（头部更亮）
        color = COLORS["SNAKE_HEAD"] if i == 0 else COLORS["SNAKE_BODY"]
        # 绘制带圆角的蛇身
        pygame.draw.rect(screen, color, (x, y, CELL_SIZE - 1, CELL_SIZE - 1), border_radius=4)

    # 绘制食物（使用圆形）
    center = (food_pos[0] + CELL_SIZE // 2, food_pos[1] + CELL_SIZE // 2)
    pygame.draw.circle(screen, COLORS["RED"], center, CELL_SIZE // 2 - 2)

    # 显示分数信息
    show_text(f"分数: {score}  最高分: {high_score}", 24, COLORS["WHITE"], (10, 10))

    # 游戏结束显示提示
    if not is_playing:
        text_width = 400  # 根据文字长度估算居中位置
        show_text("游戏结束！按 R 重新开始", 48, COLORS["WHITE"],
                  (WINDOW_WIDTH // 2 - text_width // 2, WINDOW_HEIGHT // 2 - 30))

    # 更新画面并控制游戏速度
    pygame.display.update()
    # 根据加速状态动态调整帧率
    pygame.time.Clock().tick(ACCELERATE_FPS if accelerate else BASE_FPS)
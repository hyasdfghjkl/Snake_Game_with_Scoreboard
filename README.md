# Snake_Game_with_Scoreboard

好的，以下是适合放在 GitHub 仓库中的 README.md 文件内容，采用了 Markdown 格式，符合 GitHub 的显示规范：
markdown复制
# 贪吃蛇大作战

![Python](https://img.shields.io/badge/Python-3.8-blue)
![Pygame](https://img.shields.io/badge/Pygame-2.0.0-red)
![License](https://img.shields.io/badge/License-MIT-green)

一个基于 Python 和 Pygame 开发的简单贪吃蛇游戏。玩家通过控制蛇的移动方向，吃掉食物，同时避免撞到墙壁或自身身体。游戏支持加速功能，并记录分数和历史最高分。

## 📸 游戏截图
![Game Screenshot](https://via.placeholder.com/800x600.png?text=贪吃蛇+游戏+界面)
*（请替换为实际游戏截图）*

## 🚀 功能特点
1. **蛇的控制**：
   - 使用方向键（↑、↓、←、→）控制蛇的移动方向。
   - 按住方向键可以加速蛇的移动。
2. **游戏逻辑**：
   - 蛇吃到食物后，身体会变长，分数增加 10 分。
   - 如果蛇撞到墙壁或自身身体，游戏结束。
3. **分数记录**：
   - 游戏会记录当前分数和历史最高分。
   - 历史最高分会保存在 `highscore.txt` 文件中。
4. **快捷键**：
   - `Q` 键：退出游戏。
   - `R` 键：在游戏结束后重新开始游戏。

## 🖥️ 运行环境
- Python 3.x
- Pygame 库（可通过 `pip install pygame` 安装）

## 🛠️ 安装与运行
1. 克隆或下载本项目到本地。
2. 打开终端，导航到项目目录：
   ```bash
   cd 贪吃蛇大作战
安装依赖：
bash复制
pip install pygame
运行游戏：
bash复制
python main.py
📁 项目结构
plaintext复制
贪吃蛇大作战/
├── main.py            # 主程序文件
├── highscore.txt      # 保存历史最高分的文件
📖 游戏说明
网格背景：窗口大小为 800x600 像素，网格单元格大小为 20x20 像素。
蛇的颜色：
蛇头：绿色（#00FF00）
蛇身：深绿色（#00C800）
食物：红色圆形，位于网格单元格中心。
📈 分数规则
每吃到一个食物，分数增加 10 分。
历史最高分会保存在 highscore.txt 文件中，游戏结束后会自动更新。
🔄 如何重新开始
游戏结束后，按 R 键可以重新开始游戏。
按 Q 键随时退出游戏。
🛡️ 开源协议
本项目采用 MIT License 开源协议，欢迎自由使用和修改。
📫 联系方式
作者：[你的名字]
邮箱：[你的邮箱地址]
GitHub：[你的 GitHub 地址]
如果有任何问题或建议，欢迎提交 Issue 或 Pull Request！
复制

### 说明：
1. **截图**：请将游戏的实际截图替换到 `[Game Screenshot]` 部分。
2. **作者信息**：替换 `你的名字`、`你的邮箱地址` 和 `你的 GitHub 地址`。
3. **仓库链接**：在 `Issue` 部分替换为你的 GitHub 仓库地址。

将此文件保存为 `README.md` 并上传到你的 GitHub 仓库中即可。

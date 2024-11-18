import board
from digitalio import DigitalInOut, Direction
from adafruit_rgb_display import st7789

mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        cell_width = self.game.width // len(self.mini_map[0])
        cell_height = self.game.height // len(self.mini_map)

        # 색상 정의
        COLORS = {
            1: (255, 0, 0),  # 벽: 빨간색
            0: (0, 0, 255),  # 빈 공간: 파란색
        }

        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                color = COLORS.get(value, (0, 0, 0))  # 기본값 검정색
                x1 = i * cell_width
                y1 = j * cell_height
                x2 = x1 + cell_width - 1
                y2 = y1 + cell_height - 1

                if value == 1:
                    self.game.draw.rectangle([x1, y1, x2, y2], fill=color, outline=(0, 0, 0))
                else:
                     self.game.draw.rectangle([x1, y1, x2, y2], fill=color)

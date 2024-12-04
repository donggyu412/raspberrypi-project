from PIL import ImageDraw

_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, _, _, _, _, _, _, 2, _, 2, _, 1],
    [1, _, 1, 1, 1, 1, 1, 1, _, 1, _, 2, _, 1],
    [1, _, 1, _, _, _, _, _, _, 1, _, 2, _, 1],
    [1, _, 1, _, 1, _, 1, 2, 2, 1, _, 2, _, 1],
    [1, _, _, _, 2, _, 1, _, _, _, _, _, _, 1],
    [1, 2, 1, _, 2, _, _, 2, 2, 2, 2, _, 1, 1],
    [1, _, _, _, 2, 2, _, _, _, _, _, _, _, 1],
    [1, _, 1, _, 2, _, 2, _, 2, 2, 2, 2, _, 1],
    [1, _, 2, _, _, _, 2, _, _, _, _, _, _, 1],
    [1, 1, 2, 1, 1, 1, 2, _, 2, 2, 2, 2, 2, 1],
    [1, _, 2, _, _, _, 1, _, 2, _, _, _, 2, 1],
    [1, _, _, _, 1, _, _, _, _, _, 2, _, _, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.rows = len(self.mini_map)
        self.cols = len(self.mini_map[0])
        self.cell_size = self.game.display.width // self.cols  # 셀 크기 자동 조정
        self.get_map()

    def get_map(self):
        """맵 데이터를 읽어들여 월드 맵에 저장"""
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value


    def draw(self):
        draw = ImageDraw.Draw(self.game.image)
        for pos in self.world_map:
            x, y = pos
            rect = (x * self.cell_size, y * self.cell_size,
                    (x + 1) * self.cell_size, (y + 1) * self.cell_size)
            draw.rectangle(rect, outline="gray")

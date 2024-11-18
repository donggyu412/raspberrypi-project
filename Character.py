class Character:
    def __init__(self, width, height, x=120, y=120, radius=10, color=(0, 255, 0)):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def move(self, dx, dy):

        self.x = max(self.radius, min(self.width - self.radius, self.x + dx))
        self.y = max(self.radius, min(self.height - self.radius, self.y + dy))

    def draw(self, draw):

        x1 = self.x - self.radius
        y1 = self.y - self.radius
        x2 = self.x + self.radius
        y2 = self.y + self.radius
        draw.ellipse([x1, y1, x2, y2], fill=self.color)

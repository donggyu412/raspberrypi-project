from PIL import Image
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.image
        self.textures = self.load_wall_textures()

    def draw(self):
        pass 

    def draw_wall(self, ray, proj_height, texture_id):
        texture = self.textures[texture_id]
        texture = texture.resize((SCALE, int(proj_height)))
        pos = (ray * SCALE, HALF_HEIGHT - int(proj_height) // 2)
        self.screen.paste(texture, pos)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
        }

    def get_texture(self, path):
        try:
            return Image.open(path).convert('RGBA')
            print(f"텍스처 로드 성공: {path}")
        except Exception as e:
            print(f"텍스처 로드 오류: {path}, {e}")
            return Image.new('RGBA', (TEXTURE_SIZE, TEXTURE_SIZE))
        
    def render_game_objects(self):
        for depth, image, pos in sorted(self.game.raycasting.objects_to_render, key=lambda x: x[0], reverse=True):
            self.screen.paste(image, (int(pos[0]), int(pos[1])))

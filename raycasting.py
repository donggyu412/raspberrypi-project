import math
from settings import *

class RayCasting:
    def __init__(self, game):
        self.game = game
        self.objects_to_render = []

    def update(self):
        self.objects_to_render = []
        ox, oy = self.game.player.pos

        ray_angle = self.game.player.angle - HALF_FOV
        for ray in range(NUM_RAYS):
            sin_a = math.sin(ray_angle)
            cos_a = math.cos(ray_angle)

            depth = 0
            hit = False
            while depth < MAX_DEPTH:
                depth += 0.02
                x = ox + depth * cos_a
                y = oy + depth * sin_a

                if (int(x), int(y)) in self.game.map.world_map:
                    hit = True
                    texture_id = self.game.map.world_map[(int(x), int(y))]
                    texture = self.game.object_renderer.textures[texture_id]

                    # 수직선 왜곡 보정
                    correct_depth = depth * math.cos(ray_angle - self.game.player.angle)

                    # 투영 높이 계산
                    proj_height = SCREEN_DIST / (correct_depth + 0.0001)

                    # 이미지 크기 조정
                    image = texture.resize((SCALE, int(proj_height)))

                    # 위치 계산
                    x_pos = ray * SCALE
                    y_pos = HALF_HEIGHT - int(proj_height) // 2

                    # 렌더링 객체 추가
                    self.objects_to_render.append((correct_depth, image, (x_pos, y_pos)))
                    break

            if not hit:
                print(f"Ray {ray}: 벽과 충돌하지 않음")

            ray_angle += DELTA_ANGLE
        print(f"Objects to render: {len(self.objects_to_render)}")

from settings import *
import math

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False

    def move(self, dx, dy):
        next_x = self.x + dx
        next_y = self.y + dy

        can_move_x, wall_type_x = self.check_wall(next_x, self.y)
        if can_move_x:
            self.x = next_x
        else:
            self.handle_collision(wall_type_x)

        can_move_y, wall_type_y = self.check_wall(self.x, next_y)
        if can_move_y:
            self.y = next_y
        else:
            self.handle_collision(wall_type_y)


    def move_forward(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        speed = PLAYER_SPEED * self.game.delta_time
        dx = cos_a * speed
        dy = sin_a * speed
        self.move(dx, dy)

    def move_backward(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        speed = PLAYER_SPEED * self.game.delta_time
        dx = -cos_a * speed
        dy = -sin_a * speed
        self.move(dx, dy)

    def rotate_left(self):
        self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def rotate_right(self):
        self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        """벽 충돌 검사 및 벽의 종류 반환"""
        x_int, y_int = int(x), int(y)
        if (x_int, y_int) in self.game.map.world_map:
            wall_type = self.game.map.world_map[(x_int, y_int)]
            return False, wall_type  # 벽이 있을 경우 False와 벽의 종류 반환
        return True, None  # 벽이 없을 경우 True와 None 반환
    
    def handle_collision(self, wall_type):
        """벽과 충돌 시 처리"""
        if wall_type == 2:
            # 일반 벽과의 충돌 처리 (필요하다면 추가 로직)
            pass
        elif wall_type == 3:
            # 게임 클리어 벽과 충돌한 경우
            self.game.game_clear()

    def update(self):
        pass

    @property
    def pos(self):
        """현재 위치 반환"""
        return self.x, self.y

    @property
    def map_pos(self):
        """맵 좌표 반환"""
        return int(self.x), int(self.y)

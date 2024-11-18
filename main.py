import time
from setting import setup_display, create_image
from Character import Character
from Joystick import Joystick
import importlib
import game_map

class Game:
    def __init__(self):
        # 디스플레이 설정
        self.disp = setup_display()
        self.joystick = Joystick()  

        # 이미지와 그리기 도구 생성
        self.width = self.disp.width
        self.height = self.disp.height
        self.image, self.draw = create_image(self.width, self.height)

        # 캐릭터 생성
        self.character = Character(self.width, self.height)

        # 맵 객체 생성
        self.map = game_map.Map(self)

    def update(self):
        direction = self.joystick.get_direction()
        if direction == "UP":
            self.character.move(0, -5)
        elif direction == "DOWN":
            self.character.move(0, 5)
        elif direction == "LEFT":
            self.character.move(-5, 0)
        elif direction == "RIGHT":
            self.character.move(5, 0)

    def draw_frame(self):
        # 이전 프레임 지우기
        self.image, self.draw = create_image(self.width, self.height)

        # 맵과 캐릭터 그리기
        self.map.draw()
        self.character.draw(self.draw)

        # 화면 업데이트
        self.disp.image(self.image)

    def run(self):
        try:
            while True:
                # 상태 업데이트
                self.update()

                # 화면 그리기
                self.draw_frame()

                # 일정 시간 대기
                time.sleep(0.1)

        except KeyboardInterrupt:
            print("프로그램 종료.")
            return

if __name__ == '__main__':
    game = Game()
    game.run()

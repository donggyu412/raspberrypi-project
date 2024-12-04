import board
from digitalio import DigitalInOut, Direction
from adafruit_rgb_display import st7789
from PIL import Image, ImageDraw
from map import Map
from player import Player
from raycasting import RayCasting
from object_renderer import ObjectRenderer
import pygame as pg
import sys

class Game:
    def __init__(self):
        # ST7789 디스플레이 설정
        cs_pin = DigitalInOut(board.CE0)
        dc_pin = DigitalInOut(board.D25)
        reset_pin = DigitalInOut(board.D24)
        BAUDRATE = 24000000

        #백라이트 설정
        backlight = DigitalInOut(board.D26)
        backlight.switch_to_output()
        backlight.value = True

        spi = board.SPI()
        self.display = st7789.ST7789(
            spi,
            height=240,
            y_offset=80,
            rotation=180,
            cs=cs_pin,
            dc=dc_pin,
            rst=reset_pin,
            baudrate=BAUDRATE,
        )

        # Pillow 이미지 초기화
        self.image = Image.new("RGB", (self.display.width, self.display.height))
        self.drawer = ImageDraw.Draw(self.image)

        # GPIO 버튼 설정
        self.button_U = DigitalInOut(board.D17)
        self.button_D = DigitalInOut(board.D22)
        self.button_L = DigitalInOut(board.D27)
        self.button_R = DigitalInOut(board.D23)
        self.button_A = DigitalInOut(board.D5)

        for button in [self.button_U, self.button_D, self.button_L, self.button_R, self.button_A]:
            button.direction = Direction.INPUT

        # Pygame 초기화
        pg.init()
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)


    def update(self):
        self.player.update()
        self.raycasting.update()
        self.delta_time = self.clock.tick(30)/1000.0

    def draw(self):
        self.drawer.rectangle((0, 0, self.display.width, self.display.height), fill="black")
        # 필요한 렌더링 함수 호출
        self.object_renderer.render_game_objects()
        self.display.image(self.image)


    def check_events(self):
        if not self.button_U.value:
            self.player.move_forward()  # 위로 이동
            #print("앞")
        if not self.button_D.value:
            self.player.move_backward()  # 아래로 이동
            #print("뒤")
        if not self.button_L.value:
            self.player.rotate_left()  # 왼쪽 회전
        if not self.button_R.value:
            self.player.rotate_right()  # 오른쪽 회전

    def game_clear(self):
        """게임 클리어 상태 처리"""
        # 게임 클리어 이미지를 로드합니다.
        clear_image = Image.open('resources/textures/victory.png').convert("RGBA")
        clear_image = clear_image.resize((self.display.width, self.display.height))
        self.image.paste(clear_image, (0, 0))
        self.display.image(self.image)

        # 게임 루프를 일시 정지하고, 'A' 버튼 입력을 대기합니다.
        self.wait_for_restart()

    def wait_for_restart(self):
        """게임 재시작을 위한 입력 대기"""
        while True:
            # 'A' 버튼 입력을 대기합니다.
            if not self.button_A.value:
                # 게임을 재시작합니다.
                self.new_game()
                break
            # 짧은 시간 대기하여 CPU 사용률을 낮춥니다.
            pg.time.delay(100)


    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == "__main__":
    try:
        game = Game()
        game.run()
    except KeyboardInterrupt:
        pg.quit()
        sys.exit()

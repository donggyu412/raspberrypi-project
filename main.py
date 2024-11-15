import board    
import time                                # 라즈베리파이의 핀을 다룰수 있게 해줌
from digitalio import DigitalInOut, Direction   # 버튼과 불을 켜는 것을 다루기 위해 필요
from PIL import Image, ImageDraw                # 그림을 그리고 글씨를 쓸수있게 해줌
from adafruit_rgb_display import st7789         # 화면에 그림을 그릴수 있게 해줌
from game_map import Map

class Game:
    def __init__(self):
        cs_pin = DigitalInOut(board.CE0)
        dc_pin = DigitalInOut(board.D25)
        reset_pin = DigitalInOut(board.D24)
        BAUDRATE = 24000000

        spi = board.SPI()
        self.disp = st7789.ST7789(
            spi,
            width=240,
            height=240,
            y_offset=80,
            rotation=180,
            cs=cs_pin,      
            dc=dc_pin,
            rst=reset_pin,
            baudrate=BAUDRATE,
        )

        # 필수 백라이트 켜기 LCD 디스플레이는 스스로 빛을 내지 않기 때문에 
        backlight = DigitalInOut(board.D26)
        backlight.switch_to_output()
        backlight.value = True

        # Create blank image for drawing.
        # Make sure to create image with mode 'RGB' for color.
        self.width = self.disp.width
        self.height = self.disp.height
        self.image = Image.new("RGB", (self.width, self.height), color=(0, 0, 0))  # 검정 배경
        self.draw = ImageDraw.Draw(self.image)  # 그리기 도구

        self.map = Map(self)  # 맵 객체 생성

    def run(self):
        while True:
            self.map.draw()  # 맵 그리기
            self.disp.image(self.image)  # 디스플레이에 이미지 출력
            time.sleep(0.1)


if __name__ == '__main__':
    game = Game()
    game.run()

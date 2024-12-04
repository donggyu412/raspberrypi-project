import board
import digitalio
from adafruit_rgb_display import st7789
from PIL import Image

class ST7789Display:
    def __init__(self):
        # 디스플레이 초기화
        self.cs_pin = digitalio.DigitalInOut(board.CE0)
        self.dc_pin = digitalio.DigitalInOut(board.D25)
        self.reset_pin = digitalio.DigitalInOut(board.D24)
        self.spi = board.SPI()  # self.spi로 저장하여 클래스 내에서 사용 가능

        self.disp = st7789.ST7789(
            self.spi,
            height=240,
            width=240,
            y_offset=80,  
            rotation=180,  # 회전 설정
            cs=self.cs_pin,
            dc=self.dc_pin,
            rst=self.reset_pin,
            baudrate=24000000,
        )

        # 화면 크기 설정
        self.width = self.disp.width
        self.height = self.disp.height

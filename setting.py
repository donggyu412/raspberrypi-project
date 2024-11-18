import board
from digitalio import DigitalInOut
from PIL import Image, ImageDraw
from adafruit_rgb_display import st7789

def setup_display():
    cs_pin = DigitalInOut(board.CE0)
    dc_pin = DigitalInOut(board.D25)
    reset_pin = DigitalInOut(board.D24)
    BAUDRATE = 24000000

    spi = board.SPI()
    disp = st7789.ST7789(
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

    # 백라이트 설정
    backlight = DigitalInOut(board.D26)
    backlight.switch_to_output()
    backlight.value = True

    return disp

def create_image(width, height, color=(0, 0, 0)):
    image = Image.new("RGB", (width, height), color=color)
    draw = ImageDraw.Draw(image)
    return image, draw

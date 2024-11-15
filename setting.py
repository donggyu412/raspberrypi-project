


# Create the display
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)
BAUDRATE = 24000000

spi = board.SPI()
disp = st7789.ST7789(
    spi,
    width =240,
    height=240,     #디스플레이의 세로크기
    y_offset=80,    #화면의 Y축 기준 위치
    rotation=180,   #화면이 거꾸로 되어 있기 때문에 180도 돌려줌
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
width = disp.width
height = disp.height
image = Image.new("RGB", (width, height), color=(128,128,128)) #Image.new(mode, size, color=None)


# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

disp.image(image)





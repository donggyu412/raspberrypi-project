import math

# 디스플레이 해상도
RES = WIDTH, HEIGHT = 240, 240  # ST7789 디스플레이 해상도
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 30  # 프레임 속도 제한

# 플레이어 설정
PLAYER_POS = 1.5, 1.5  # mini_map
PLAYER_ANGLE = 0
PLAYER_SPEED = 2.0  # 이동 속도 조정
PLAYER_ROT_SPEED = 1.5  # 회전 속도
PLAYER_SIZE_SCALE = 30  # 플레이어 크기 조정
PLAYER_MAX_HEALTH = 100


# 바닥 색상
FLOOR_COLOR = (30, 30, 30)

# 시야(FOV) 및 레이캐스팅 관련 설정
FOV = math.pi / 3  # 시야각 60도
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2  # 레이의 수를 화면 너비에 맞게 설정
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 30
SCREEN_DIST = (WIDTH // 2) / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# 투사 관련 설정
SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

# 텍스처 크기
TEXTURE_SIZE = 64  
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2

from digitalio import DigitalInOut, Direction, Pull  
import board

class Joystick:
    def __init__(self):
        # 조이스틱 버튼 초기화
        self.button_U = DigitalInOut(board.D17)  # Up
        self.button_U.direction = Direction.INPUT
        self.button_U.pull = Pull.UP  # 풀업 저항 활성화

        self.button_D = DigitalInOut(board.D22)  # Down
        self.button_D.direction = Direction.INPUT
        self.button_D.pull = Pull.UP  # 풀업 저항 활성화

        self.button_L = DigitalInOut(board.D27)  # Left
        self.button_L.direction = Direction.INPUT
        self.button_L.pull = Pull.UP  # 풀업 저항 활성화

        self.button_R = DigitalInOut(board.D23)  # Right
        self.button_R.direction = Direction.INPUT
        self.button_R.pull = Pull.UP  # 풀업 저항 활성화

        self.button_C = DigitalInOut(board.D4)   # Center
        self.button_C.direction = Direction.INPUT
        self.button_C.pull = Pull.UP  # 풀업 저항 활성화

    def get_direction(self):
        """
        조이스틱 방향 읽기:
        - Up, Down, Left, Right, Center 중 하나를 반환
        """
        if not self.button_U.value:  # Up 버튼 눌림
            return "UP"
        elif not self.button_D.value:  # Down 버튼 눌림
            return "DOWN"
        elif not self.button_L.value:  # Left 버튼 눌림
            return "LEFT"
        elif not self.button_R.value:  # Right 버튼 눌림
            return "RIGHT"
        elif not self.button_C.value:  # Center 버튼 눌림
            return "CENTER"
        return None  # 아무 버튼도 눌리지 않음

from sense_hat import SenseHat, ACTION_HELD, ACTION_PRESSED, ACTION_RELEASED
from time import sleep
import signal
import threading
import os

# 초기화

sense = SenseHat()
sense.clear()

# 전역 변수

ydir = [-1, 1, 0, 0]
xdir = [0, 0, -1, 1]
nowPos = [0, 0]


# 조이스틱 (인터럽트 방식)


# 분업자 작성 코드

def send():
    pass


def receive():
    pass


def drawOpMap():
    pass


def drawMyMap():
    pass


# 사용할 함수 목록

def attack(nowPos):
    if (opmap[nowPos[0][nowPos[1]]] == 1):
        pass
    else:
        pass


def pushed_middle(event):
    global nowPos
    if (event.action != ACTION_PRESSED):
        attack(nowPos)


def pushed_up(event):
    global nowPos
    if (event.action != ACTION_PRESSED) and nowPos[0] > 0:
        nowPos[0] -= 1
        print(nowPos)


def pushed_down(event):
    global nowPos
    if (event.action != ACTION_PRESSED) and nowPos[0] < 7:
        nowPos[0] += 1
        print(nowPos)


def pushed_left(event):
    global nowPos
    if (event.action != ACTION_PRESSED) and nowPos[1] > 0:
        nowPos[1] -= 1
        print(nowPos)


def pushed_right(event):
    global nowPos
    if (event.action != ACTION_PRESSED) and nowPos[1] < 7:
        nowPos[1] += 1
        print(nowPos)


# 1
receive()
mymap = "0101010000000000110011000000000000111000000000001111000000000000"
opmap = "1010100000000000001100110000000000111000000000001111000000000000"

"""
3: 유효타
4: 헛타 or 힌트
"""

# 2
receive()
isMyturn = 1  # 송수신 받아서 처리, 내 차례가 아닐 경우 0

if __name__ == '__main__':
    # 3
    drawOpMap()
    sense.stick.direction_up = pushed_up
    sense.stick.direction_down = pushed_down
    sense.stick.direction_left = pushed_left
    sense.stick.direction_right = pushed_right
    sense.stick.direction_middle = pushed_middle

    signal.pause()  # 개선하자면, while로 대체할 것
    # while(1):
    #     if(isMyturn):

    #     else:

    #     sleep(1)

"""
pseudo
1. 내 맵과 상대 맵을 송수신받는다 (일단은 송수신 받았다고 가정)
2. 내 차례인지 상대 차례인지 송수신 받아 표시한다
3. 내 차례라면
    3-1. 상대 맵을 보여준다. (맵 그리는건 저쪽에서 해줄 것임)
    3-2. 조이스틱 상, 하, 좌, 우, 클릭을 이용해 맵 이동 및 공격을 구현한다 (추가기능 : 꾹 누르면 내 맵 상황 보여주기)
    3-3. 맞았으면 맞은거 보여주고(대각선 무효화된거 보여주고), 송신하고,  턴 이어가기
    3-4. 틀렸으면 틀린거 보여주고(맵 무효화 시키고) 턴 넘기고, 송신하기
4. 상대 차례라면
    4-1. 내 맵을 보여준다. (맵 그리는건 저쪽에서 해줄 것임)
    4-2. 수신하면 수신하는대로 맵을 갱신하다
    4-3. 버튼을 홀드(하거나 클릭) 하면 내 맵의 진짜 상태를 보여준다
    4-4. 턴이 끝남을 수신하면 내 차례로 넘긴다
"""
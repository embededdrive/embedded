from random import randint
import random

mymap = '00001111000001110011001110101000'





## list는 내가 초기화하는 2차원 배열
## oplist는 상대가 준 문자열로 만든 2차원 배열
list = [[0] * 8 for _ in range(8)]
oplist = [[0] * 8 for _ in range(8)]
queue=[]
dir=([-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1])


## nono 함수는 1로 할당된 배 주변에 재할당을 막기위해 2로 채워주는함수
def nono(y, x):
    for i in range(8):
        yy= y+dir[i][0]
        xx= x+dir[i][1]
        if(yy<0 or yy>=8 or xx<0 or xx>=8 or list[yy][xx]!=0):
            continue
        else:
            list[yy][xx]=2


## init들은 각 크기만큼 배를 2차원 배열에 채워줌
def init4():
    cnt= 0
    while(cnt<1):
        rl = randint(0, 1)

        if(rl==0):
            rx= randint(0,4)
            ry = randint(0,7)
            for i in range(4):
                list[ry][rx]=1

                queue.append([ry,rx])
                rx = rx +1
            for i  in range(4):
                a,b=queue.pop()


        elif(rl==1):
            rx= randint(0,7)
            ry = randint(0,4)
            for i in range(4):
                list[ry][rx]=1

                queue.append([ry,rx])
                ry = ry +1
            for i  in range(4):
                a,b =queue.pop()

        cnt = cnt+1
    
def init3():
    cnt= 0
    while(cnt<1):
        flag =0
        rl = randint(0, 1)
        if(rl==0):
            rx= randint(0,5)
            ry = randint(0,7)
            
            if(list[ry][rx]==0 and list[ry][rx+1]==0 and list[ry][rx+2]==0):
                list[ry][rx]=1
                list[ry][rx+1]=1
                list[ry][rx+2]=1
                queue.append([ry,rx])
                queue.append([ry,rx+1])
                queue.append([ry,rx+2])
                for i in range(3):
                    a,b = queue.pop(0)
                    nono(a,b)
            else:
                flag=1
        
        elif(rl==1):
            rx= randint(0,7)
            ry = randint(0,5)
            if(list[ry][rx]==0 and list[ry+1][rx]==0 and list[ry+2][rx]==0):
                list[ry][rx]=1
                list[ry+1][rx]=1
                list[ry+2][rx]=1
                queue.append([ry,rx])
                queue.append([ry+1,rx])
                queue.append([ry+2,rx])
                for i in range(3):
                    a,b = queue.pop(0)
                    nono(a,b)
            else:
                flag=1
        if(flag==1):
            continue
        cnt = cnt+1

def init2():
    cnt= 0
    while(cnt<2):
        flag =0
        rl = randint(0, 1)
        if(rl==0):
            rx= randint(0,6)
            ry = randint(0,7)
            
            if(list[ry][rx]==0 and list[ry][rx+1]==0):
                list[ry][rx]=1
                list[ry][rx+1]=1
                queue.append([ry,rx])
                queue.append([ry,rx+1])
                for i in range(2):
                    a,b = queue.pop(0)
                    nono(a,b)
            else:
                flag=1
        
        elif(rl==1):
            rx= randint(0,7)
            ry = randint(0,6)
            if(list[ry][rx]==0 and list[ry+1][rx]==0):
                list[ry][rx]=1
                list[ry+1][rx]=1
                queue.append([ry,rx])
                queue.append([ry+1,rx])
                for i in range(2):
                    a,b = queue.pop(0)
                    nono(a,b)
            else:
                flag=1
        if(flag==1):
            continue
        cnt = cnt+1

def init1():
    cnt= 0
    while(cnt<3):
        flag =0
        rx= randint(0,7)
        ry = randint(0,7)
            
        if(list[ry][rx]==0):
            list[ry][rx]=1
            queue.append([ry,rx])
            (a,b) = queue.pop(0)
            nono(a,b)
        else:
            flag=1
        
        if(flag==1):
            continue
        cnt = cnt+1

## 4,3,2,1 크기의 배들 초기화
init4()
print("초기화완료")
init3()
print("초기화완료")
init2()
print("초기화완료")
init1()
stmap = ''
print("초기화완료")
for i in range(8):
    for j in range(8):
        if(list[i][j]==0):
            stmap = stmap + '0'
        elif(list[i][j]==1):
            stmap = stmap + '1'
        else:
            continue ## 0이랑 1아닌 값들은 초기에 받는경우가 없고 보낼필요도없다
print(stmap)
# 문자열 받은부분을 맵에 할당


for i in range(8):
    for j in range(8):
        oplist[i][j] = mymap[8*i+j]


# ## 센스햇에 내맵 확인
from sense_hat import SenseHat

list = [[0,0,1,1,0,0,0,0],[3,3,0,0,4,4,0,0,0,0],[3,3,0,0,4,4,0,0,0,0],[3,3,0,0,4,4,0,0,0,0],[3,3,0,0,4,4,0,0,0,0],[3,3,0,0,4,4,0,0,0,0],[3,3,0,0,4,4,0,0,0,0],[3,3,0,0,4,4,0,0,0,0]]

hat = SenseHat()

def update_screen():
    hat.clear()
    for i in range(8):
        for j in range(8):
            if(list[i][j]==1):
                hat.set_pixel(i, j, 255, 255, 255)
            elif(list[i][j]==3): ##유효타시 빨간색
                hat.set_pixel(i, j, 255, 0, 0)
            elif(list[i][j]==4): ## 헛타는 초록색
                hat.set_pixel(i, j, 0, 255, 0)
    


update_screen()
while True:
    for event in hat.stick.get_events():

        update_screen()


# 실제 게임을 하는 맵
from sense_hat import SenseHat
oplist =[
    [1,1,0,0,1,1,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
x = y = 5
hat = SenseHat()

def update_screen():
    hat.clear()
    
    for i in range(8):
        for j in range(8):
            
            if(oplist[i][j]==3):
                hat.set_pixel(i, j, 255, 0, 0)
            elif(oplist[i][j]==4):
                hat.set_pixel(i, j, 0, 255, 0)
    hat.set_pixel(y, x, 255, 255, 255)


def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def move_dot(event):
    global x, y
    if event.action in ('pressed', 'held'):
        if(event.direction == 'middle'):
            print("눌림") ## 가운데 버튼 누르면 oplist 배열 수정
            if(oplist[y][x]==1):
                print("맞춤")
                oplist[y][x]=3 ## 정타
            elif(oplist[y][x]==0):
                print("못맞")
                oplist[y][x]=4 ## 헛방
        x = clamp(x + {
            'left': -1,
            'right': 1,
            }.get(event.direction, 0))
        y = clamp(y + {
            'up': -1,
            'down': 1,
            }.get(event.direction, 0))


update_screen()
while True:
    for event in hat.stick.get_events():
        move_dot(event)
        update_screen()
import turtle
import math

def turnleft(): #왼쪽으로 5도 꺾는 함수
    player.left(5)

def turnright(): #오른쪽으로 5도 꺾는 함수
    player.right(5)

def fire(): #발사 함수
    x = player.xcor() #현재 x좌표 저장
    y = player.ycor() #현재 y좌표 저장
    velocity = 80 #속도 80
    angle = player.heading() #현재 각도 저장
    vx = velocity * math.cos(angle * 3.14 / 180.0) #x방향 속도 저장
    vy = velocity * math.sin(angle * 3.14 / 180.0) #y방향 속도 저장
    while player.ycor() >= 0 : #현재 y좌표가 음수가 되기 전 까지 반복
        vx = vx #x방향은 등속도 운동이므로 변화 없음
        vy = vy - 10  #y방향은 등가속도 운동이므로 속도 10씩 감소
        x = x + vx #x방향 이동거리 더해줌
        y = y + vy #y방향 이동거리 더해줌
        player.goto(x,y) #x,y 위치로 이동

player = turtle.Pen()
player.shape("turtle")
screen = player.getscreen() #이벤트 감지를 위한 스크린 생성

screen.onkeypress(turnleft,"Left") #왼쪽 방향키 누르면 함수 실행
screen.onkeypress(turnright,"Right") #오른쪽 방향키 누르면 함수 실행
screen.onkeypress(fire,"space") #스페이스바 누르면 발사함수 실행

player.goto(+300,0) #그래프 만들기
player.goto(-300,0)
player.goto(-300,300)
player.goto(-300,0)
screen.listen() #이벤트 감지
import turtle

t = turtle.Turtle()
square = [500,500]
colors = ["red","orange","yellow","green","blue","navy"] #막대그래프, Pie그래프

def turtleAxis(): #축
    t.speed(0)
    t.left(90)
    t.forward(square[1]-65)
    t.setpos(0, 0)
    t.right(90)
    t.forward(square[1]-65)
    t.setpos(0, 0)

def turtleIndex(): #범례
    t.penup()
    t.setpos(0,-30)
    t.pendown()
    idx=0
    for _ in colors:
        t.color(colors[idx]) #펜 색상을 colors로 변경
        t.pensize(1) #펜 굵기를 1로 변경
        t.pendown()
        #범례 사각형 그리기
        for i in range(4):
            t.forward(5)
            t.left(90)
        #옆에 설명 쓰기
        t.penup()
        t.forward(10)
        t.pendown()
        t.write(f"a[{idx}]", font = ("Times New Roman", 10, "bold"))
        t.penup()
        t.forward(20)
        idx+=1

def turtleBar(a): #막대그래프
    t.reset()
    turtleAxis()
    square = [300,300]
    idx = 0
    sum = 0
    for v in a:
        sum += v
    for height in a:
        t.begin_fill()
        t.fillcolor(colors[idx])#채우기 시작
        idx+=1
        t.left(90)
        #막대그래프를 그린다
        t.forward((height/sum)*square[0])
        x = t.xcor()
        y = t.ycor()
        t.penup()
        t.setpos(0,(height/sum)*square[0]) #해당비율만큼 그린다
        t.write(str(height), False, "right", ("Times New Roman",8,"bold"))
        t.setpos(x,y)
        t.pendown()
        t.right(90)
        t.forward(25)
        t.right(90)
        t.forward((height/sum)*square[0]) #해당비율만큼 그린다
        t.left(90)
        t.end_fill() #채우기 끝
        t.hideturtle() #커서가 보이지 않게한다.
    turtleIndex()

def turtlePie(a): #파이그래프
    t.reset()
    sum = 0
    num = 0
    percentages = []
    t.speed(0)
    n = len(a)
    for v in a:
        sum += v 
    for v in a:
        percentages.append(v/sum) #비율대로 그리기 위해 비율을 따로 리스트에 저장한다.
    radius = 100
    my_start = t.position() #원의 중점위치를 따로 변수에 저장한다.
    for percent in percentages:  #arc(호) 단위 하나씩 반복과정으로 그린다
        t.begin_fill()
        t.fillcolor(colors[num])
        t.write(str(round((percent*100),0))+"%", False, "left", ("Times New Roman",10,"bold"))
        t.circle(radius,(percent*360)) #해당 각도만큼만 호를 그린다
        t.left(90)
        t.forward(radius)
        t.left(180)
        t.right(percent*360)
        t.forward(radius)
        t.end_fill()
        t.left(90)
        my_start = t.position() #그다음 호를 위해 커서 이동
        t.circle(radius,percent*360)
        num+=1
    t.hideturtle()
    turtleIndex()


#main 함수
if __name__ == "__main__":
    turtle.setup(square[0], square[1],0,0) #만약 +width라는 가변변수에 data
    turtleBar([10, 20, 30, 20, 10])
    turtlePie([10, 20, 30, 20, 10])
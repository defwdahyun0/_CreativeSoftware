Turtle_Graph는 창의소프트웨어 입문 과목에서 부여된 파이썬 turtle module을 이용해서 그래프를 그리는 과제이다.

youtube.com/watch?v=JHAcgz4XUK0&t=1085s
위 링크의 강의를 듣고 turtle에 대해 이해한뒤,코드를 짜보았다.
 
 turtle_graph.py는 함수 turtleBar(a), turtlePie(a)를 중심적으로 구현했다.(a는 리스트이다.)
두 함수는 화면을 지우고 입력된 데이터에 대해서 막대그래프 혹은 파이그래프를 그린다.

나는 그래프를 보는 사람이 쉽게 이해할 수 있도록, 눈금선과 범례를 추가했다.
축을 그리는 함수 turtleAxis, 범례를 그리는 함수 turtleIndex를 추가했다.

샘플 데이터 a = [10, 20, 30, 20, 10] 데이터를 이용해서 그린다.
# 3x3 magic squre
3x3 마방진을 파이썬으로 구현하는 과제이다. 

3x3 마방진은 9개 간에 1~9까지 숫자를 한번씩 넣어 가로 세로 대각선의 합이 모두 같도록 한다.

## 코드 구현 과정
a b c

d e f

g h i

의 형태이다.

for문으로 abcdefghi를 가져온 후, if문 조건을 추가해서 마방진 조건에 맞는 것을 출력하도록 했다.

## 마방진 조건

### step1 
3x3 마방진에서 행/열/대각선의 합은 15
### step2
합이 15가 되려면 개수가 제한적 (1+5+9, 1+6+8, 2+4+9, 2+5+8, 2+6+7, 3+4+8, 3+5+7, 4+5+6)
### step3 
사각형의 센터는 5
### step4 
코너는 짝수(2,4,6,8), 모서리는 홀수(1,3,7,9)
### step5 
위 조건으로 8개의 행렬 존재가능 4*2

## 요구사항

1) 주어진 3x3.py 코드의 print와  시간측정 코드(time)를 그대로 사용했다.
2) 정확한 답이 나오도록 했고, 답은 8개가 나왔다.
3) git의 자신의 python 프로젝트 폴더로 magic_square_3x3폴더를 만들어 그 안에 코드와 readme.md를 저장했다. 
4) 아주 BB에 자신의 코드와 git URL을 제출했다.

5) 코드의 길이(줄수)가 가장 짧도록 만들었다. print문을 그대로 사용해야 했기 때문에 for문을 그대로 사용했고, 조건문도 필수 조건 한 줄을 추가했다.
6) 코드의 수행 시간이 가장 짧도록 만들었다. for문의 범위를 좁혀 for문에서 최소한의 범위만을 돌도록 만들었다. 수행시간은 평균적으로 0.2초 내외였다.
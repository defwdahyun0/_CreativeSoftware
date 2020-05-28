#실습
file = open("output.txt","w")
file.write("ABCDEF")
file.write(str(100)) #string만 쓸 수 있음. 숫자는 안됨
file.close()
# 줄바꿈은 안됨

file = open("output.txt","r",encoding='utf-8') #encoding, utf-8 
#encoding='ascii', errors=ignore로 하면 ascii로 출력 가능

string = file.read()
print(string)
file.close()

#with과 context manager. 
# with은 context manager 덕분에 코드 블록이 끝날 때 file.closer()가 자동호출된다.

#open() 함수의 매개 변수는 모두 9개
#file은 파일의 경로를 나태내는 문자열 혹은 이미 생성해놓은 파일 객체의 파일 기술자(file 객체의 fileno)

#binary 파일을 쓰기 위해서 struct 사용. pack 원하는 형식으로 저장
import struct
p = struct.pack('i',10*256*256*256+33*256*256+88*256+99)
for b in p: #for loop 거꾸로 돔
    print(b) #binary 
val = 10*256*256*256+33*256*256+88*256+99
print(val)
print(hex(val))
struct.unpack('i',p) #unpack을 하면 tuple이 나옴
#floating point를 pack해서 넣기
f = struct.pack('f',0.0) #\뭐지?
aaa = struct.unpack('i',f)
print(aaa)
bin(aaa[0]) #int 0도 bit에서 0000000000
#pack으로 묶은 다음에 보내기
#parameter을 조합해서 쓸 수 있음.

#추가 수업
file = open("input.txt",encoding='utf-8') #숫자로 구성된 Input.txt
type(file)
import sys
sys.stdin() #file과 같음
file2 = sys.stdin()

file.read() #다 읽어들임
file2.read() #기다림. 입력이 된 것을 출력
# fileio stdinstdout과 같은 것. 프로그램 안에서 redirection할 수도 있음

import time
time.ctime()
time.time() #시간을 확인할 수 있음

start = time._ns()
time.time_ns() - start #자신의 프로그램의 성능을 확인
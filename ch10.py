#help("Exception")
#예외 형식들은 거의 Exception  클래스로부터 파생

my_list = [1,2,3]
try:
    print("첨자를 입력하세요.")
    index = int(input())
    print(my_list[index]/0)
except Exception as err: #이 경우에는 2)3) 예외처리구문 실행할 기회가 없다
    print("예외발생했습니다. ({0})".format(err))
except ZeroDivisionError as err:
    print("0으로 나눌 수 없습니다. ({0})".format(err))
except IndexError as err:
    print("잘못된 첨자입니다. ({0})".format(err))
else: #예외 없음
    print("성공")
finally: #무조건 실행
    print("종료")

#raise 예외 일으키기
def some_function():
    print("1~10 사이의 수를 입력하세요")
    num = int(input())
    if num<1 or num>10:
        raise Exception("유효하지 않은 숫자입니다:{0}".format(num))
    else:
        print("입력한 수는{0}입니다".format(num))


#함수를 부르는 쪽에서도 error가 무엇인지 알아야할 때, 아래와 같은 함수를 만들기도 한다
def some_function_caller():
    try:
        some_function()
    except Exception as err:
        print("1) 에외가 발생했습니다. {0}".format(err))
        raise #except 절에서 예외 다시 실행
    
    try:
        some_function_caller()
    except Exception as err:
        print("2) 예외가 발생했습니다. {0}".format(err))

#직접 예외 형식 만들기
class MyException(Exception):
    def __init__(self):
        super().__init__("MyException이 발생했습니다.")

class InvalidIntException(Exception):
    def __init__(self,arg):
        super().__init__('정수가 아닙니다.:{0}'.format(arg))

def conver_to_integer(text):
    if text.isdegit(): #부호(+,-) 처리 못함
        return int(text)
    else:
        raise InvalidIntException(text)

if __name__ == '__main__':
    try:
        print("숫자를 입력하세요.")
        text = input()
        number = conver_to_integer(text)
    except InvalidIntException as err:
        print('예외가 발생했습니다.{0}'.format(err))
    else:
        print('정수 형식으로 변환되었습니다.: {0}{1}'.format(number,type(number)))

#수업 echo exception
while(True):
    try:
        a = input()
    except EOFError:
        break
    print(a) 
#ctrl+z로 끝낼 수 있다. EOF error


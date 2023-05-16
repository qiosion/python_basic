def process_error_print():
    try:
        a = [1, 2]
        print(a[3])

        b = 4 / 0
    # except:
        # print("Error 발생")
# IndexError : 인덱스 범위를 벗어날 경우
    except IndexError as e: # 인덱스 에러
        print(e) # specific 하게 이미 정의되어 있는 에러 메시지 출력
        """
        IndexError 클래스 구조
        class IndexError(Exception): # 상속
            def __str__(self):
                return "list index out of index"
        """
# ZeroDivisionError : 0으로 나눌 경우
    except ZeroDivisionError as e:
        print(e)

    # except (IndexError, ZeroDivisionError) as e:
    #     print(e)

def process_error():
    try:
        f = open("temp.txt", "r")
# FileNotFoundError : 파일이 존재하지 않을 경우
    except FileNotFoundError as e:
        print(e)
    # finally:
    #     f.close()
    print("PASS")

# Value Error : 자료형이 맞지 않을 경우
def input_age():
    while True:
        try:
            age = int(input("나이를 입력하세요: "))
            if age >= 100:
                print("99세까지만 입력가능합니다. 다시 입력해주세요")
            else:
                break
        except ValueError:
            print("다시 입력해주세요! 나이는 숫자만 입력가능합니다")
    return age

# raise 예약어를 통해 에러 발생시키기
# NotImplementedError : 상속받은 클래스가 아직 구현되지 않음
class Bird:
    def fly(self):
        raise NotImplementedError
        # pass

class Eagle(Bird): # 상속
    pass

# 사용자 정의 에러를 만들어보자 -> MyError
# Exception 클래스를 상속받아 클래스를 구현해야함
# 내장되어있는 NotImplementedError, ZeroDivisionError
class MyError(Exception):
    # pass
    def __str__(self):
        # return "허용되지 않은 별명"
        return "list 접근 불가"

def say_nick(nick):
    if nick == "stupid":
        raise MyError()
    print(nick)

def list_acceess(in_param_bool, in_param_list):
    if in_param_bool:
        print(in_param_list[:])
    else:
        raise MyError()

if __name__ == "__main__":
    """
    # process_error_print() # IndexError , ZeroDivisionError
    
    # process_error() # FileNotFoundError
    
    age = input_age() # ValueError 
    print(age)
    
    eagle = Eagle()
    eagle.fly() # NotImplementedError
    
    # 예외만들기 1 (사용자 정의 에러 MyError)
    try:
        say_nick("hello")
        say_nick("love")
        say_nick("stupid")
    except MyError as e:
        # print("허용되지 않은 별명")
        print(e)
    """
    # 예외만들기 2 (사용자 정의 에러 MyError)
    try:
        list_acceess(0, [1, 2, 3])
        list_acceess(1, [1, 2, 3])
    except MyError as e:
        print(e)

    print("end of test")
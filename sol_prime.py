# 소수 Prime Number 오류찾아 수정하기

while(1): # 무한루프
    testNum = input() # 입력
    if(testNum.isdigit()): # 숫자인지 판단
        break # 숫자면 while문을 나간다

testNum = int(testNum) # 문자열을 숫자형으로 변환

# 소수판단
for i in range(2, testNum): # 2~(testNum-1)
    print(testNum , " 나누기 ", i , " 의 나머지는 ", testNum % i)
    if(testNum % i) == 0:
        # print("i = ", i)
        print(f'{testNum} is not Prime Number')
        break
    elif(testNum-1 == i): # 나머지가 0이 아닌 상태로 입력값의 직전까지 왔으면
        # print("i = ", i)
        print(f'{testNum} is Prime Number')
# else:
#     print(f'{testNum} is Prime Number') # for-else 문
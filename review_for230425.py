def sol1(param1):
    result = [0, 0, 0, 0, 0, 0]
    for i in param1:
        if i == "XS":
            result[0] += 1
        elif i == "S":
            result[1] += 1
        elif i == "M":
            result[2] += 1
        elif i == "L":
            result[3] += 1
        elif i == "XL":
            result[4] += 1
        elif i == "XXL":
            result[5] += 1
    return result

def sol2(param2):
    result = []
    length = len(param2)
    for i in param2:
        result.append(length - i - 1)
    return result

def sol3(param3):
    result = 0
    test = 2
    for i in range(0, param3):
        test = (4 * i) + 2
        result += test
    return result

def sol4(param):
    length = len(param)
    result = 0
    max = 1
    min = length
    for i in range(0, length):
        cnt = 0
        for j in range(0, length):
            if param[i] == param[j]:
                cnt += 1
        if cnt > max:
            max = cnt
        if cnt < min:
            min = cnt
    result = int(max / min)
    return result

param1 = {"XL", "XXL", "S", "XS"}
test1 = sol1(param1)
print(test1)

param2 = [1, 4, 2, 3, -9999]
test2 = sol2(param2)
print(test2)

param3 = 3
test3 = sol3(param3)
print(param3, "항 까지의 합은 ", test3)

param4 = [1,2,3,3,1,3,3,2,3,2]
test4 = sol4(param4)
print("가장 작은 원소와 가장 큰 원소는 ", test4, "배 차이")
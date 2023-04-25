def str_split1(input_str):
    result = input_str.split()
    return result

# def str_split2(input_str):
#     result = []
#     # print("길이: ", len(input_str))
#     idx = len(input_str) -1
#     for i in range(0, len(input_str)):
#         idx = input_str.find(" ")
#         # print("i : ", i, "input_str[i] : ", input_str[i])
#     str1 = input_str[:idx]
#     input_str = input_str[idx+1:]
#     print(str1)
#     print(input_str)
#     for i in range(idx, len(input_str)):
#         idx = input_str.find(" ")
#     str2 = input_str[:idx]
#     print(str2)
#         # cnt = input_str.count(" ")
#         # print(idx)
#         # print(cnt)
#         #     result.append(input_str[:i])
#         # resultappend(input_str[0:2])
#     return result
# def str_split3(input_str):
#     cnt = input_str.count(" ")
#     idx = input_str.find(" ")
#     for i in  range(0, cnt):
#         print(i")
#
# def str_split4(input_str):
#     idx = input_str.find(" ")
#     for i in enumerate(input_str):
#         if input_str[i] == " ":
#             print("공백")
#             str = input_str[:i]
#         print(str)
# def str_split5(input_str):
#     result = []
#     str2 = input_str
#     idx = str2.find(" ")
#     for i in range(0, len(input_str)):
#         print("인덱스 : ", idx)
#         # print("밖에서 : ", input_str)
#         if i == idx:
#             str = str2[:idx]
#             result.append(str)
#             str2 = str2[idx+1:]
#             # idx = str2.find(" ")
#             print(str)
#             print("새로운 str : ", str2)
#         elif i == len(str2) - 1:
#             print("???")
#             str = str2[:]
#             print(str , "elif")
#             result.append(str)
#     return result

def str_split(input_str):
    result = []
    str2 = input_str
    idx = str2.find(" ")
    for i in input_str:
        if i == " ":
            str = str2[:idx]
            result.append(str)
            str2 = str2[idx+1:]
            idx = str2.find(" ")
        elif i == str2[-1]:
            str = str2[:]
            result.append(str)
    return result
str_test = "abrc dwaegefee ghij klmnrstj ㅈㄴ도옫"
str_test2 = "abc def      ghij klmn "
print(str_split(str_test))

input_list = [1, 2, 3, 5, 6, 9]
def impl_pop(index):
    global length
    length = len(input_list)
    if index >= length:
        print("-1")
    else:
        result = input_list.pop(index)
        length -= 1
        return result
print(f'{impl_pop(index=-1)}, {input_list}')
print(f'{impl_pop(3)}, {input_list}')
print(f'{impl_pop(4)}, {input_list}')


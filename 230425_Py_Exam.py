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

str_test = "abrc dwaegefee ghij klmnrstj"
str_test2 = "abc def      ghij klmn "
print(str_split(str_test))


input_list = [1, 2, 3, 5, 6, 9]

def impl_pop(index=-1):
    global input_list
    length = len(input_list)
    if index == -1:
        value = input_list[-1]
        input_list.remove(value)
        return value
    elif index >= 0 and index < length:
        value = input_list[index]
        input_list.remove(value)
        return value
    else:
        return -1

print(impl_pop(), input_list)
print(impl_pop(3), input_list)
print(impl_pop(4), input_list)
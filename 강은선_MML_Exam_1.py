def my_max(input_list):
    max = 0
    for var in input_list:
        if max < var:
            max = var
    return max
def prime_factorization(input_num):
    n = 2
    prime_factor = []

    while n <= input_num:
        if input_num % n == 0:
            prime_factor.append(n)
            input_num = input_num // n
        else:
            n = n + 1

    rtn_value = set(prime_factor)
    return my_max(rtn_value)

print("input num : ", end="")
input_num = int(input())

max_value = prime_factorization(input_num)
print(f'result: {max_value}')
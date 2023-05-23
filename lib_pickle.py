# 파이썬 라이브러리
# 피클 pickle
import pickle

f = open("lib_example.txt", "wb")

data = {
    '1': 'python',
    '2': 'you need'
}

pickle.dump(data, f)
f.close()

# 예외처리 try - except (with)
with open("lib_example.txt", "rb") as f:
    data = pickle.load(f)
    print(data, type(data)) # {'1': 'python', '2': 'you need'} <class 'dict'>

# 혹은 이렇게 파일을 읽어올 수 있음
f = open("lib_example.txt", "rb")
data = pickle.load(f)
print(data, type(data)) # {'1': 'python', '2': 'you need'} <class 'dict'>

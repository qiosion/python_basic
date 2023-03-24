# 문자열 슬라이싱(1) - 출력 변경
str2 = "20230307sunny"

low = str2[-5:]
# print(low) # sunny
up = low[0].upper()
weather = up + low[-4:]
# print(weather) # Sunny

rs = f'Today weather is "{weather}"'
print(rs)
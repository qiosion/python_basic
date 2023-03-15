# 문자열 슬라이싱 - 수정

str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"

# # 문자열 비교
# str_vh1 = str_txt[:17] # vehicle 0 0 50 50
# str_vh2 = str_txt[18:] # vehicle 50 50 250 250
# vh1_w = int(str_vh1[-5:-3]) # 50
# vh2_w = int(str_vh2[-7:-4]) # 250
#
# if vh1_w >= 100:
#     vh1 = str_vh1.replace("vehicle", "truck")
# if vh2_w >= 100:
#     vh2 = str_vh2.replace("vehicle", "truck")
# print(vh1)
# print(vh2)

# 리스트
str = str_txt.split()
vh1 = str[:5] # ['vehicle', '0', '0', '50', '50']
vh2 = str[5:] # ['vehicle', '50', '50', '250', '250']

if int(vh1[3]) >= 100:
    vh1[0] = 'truck'

if int(vh2[3]) >= 100:
    vh2[0] = 'truck'

print(vh1)
print(vh2)
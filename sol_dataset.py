# 문자열 슬라이싱(2) - 수정

str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"

# 리스트
str = str_txt.split()
vh1 = str[:5] # ['vehicle', '0', '0', '50', '50']
vh2 = str[5:] # ['vehicle', '50', '50', '250', '250']

if int(vh1[-2]) >= 100:
    vh1[0] = 'truck'

if int(vh2[-2]) >= 100:
    vh2[0] = 'truck'

# join을 이용해 문자열로 전환
vh1_txt = ' '.join(vh1)
vh2_txt = ' '.join(vh2)
# print(type(vh1_txt))
print(vh1_txt + vh2_txt)

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

# # range 사용 !
# str_txt = "vehicle 0 0 50 50 vehicle 50 50 250 250"
# str_list = str_txt.split()
# # print(str_list)
# for i in range(3, len(str_list), 5):
#     if int(str_list[i]) >= 100:
#         # print(str_list[i]) # w
#         str_list[i-3] = "truck" # i가 3부터 시작하니까 [0]을 찾아줌
#         # print(str_list)
#     else: # 인덱스 i 가 w값이 아닐때는 그냥 진행
#         continue
#
# # join을 이용해 문자열로 전환
# txt = ' '.join(str_list)
# # print(type(txt))
# print(txt)

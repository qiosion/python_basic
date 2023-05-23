import json
import glob
import os

# f = open("CAM_FRONT/000000.json")
# json_data = json.load(f)

# 폴더 내 모든 json 파일 가져오기
json_files = glob.glob('CAM_FRONT/*.json')

# json 파일 루프
for json_data in json_files:
    # 각각 파일 열기
    with open(json_data, 'r') as f:
        data = json.load(f)

    # 데이터 처리 작업
    processed_data = {'Image': data['Image'], 'Object': []}  # 새로 넣을 디렉터리

    for obj in data['Object']:
        # 클래스가 Dontcare 가 아니고 level 이 0인 데이터만 남기겠다
        if obj['class'] != 'Dontcare' and obj['level'] == 0:
            processed_data['Object'].append(obj)

        # Truck 과 Car 는 Vehicle 로 통일
        if obj['class'] == 'Truck' or obj['class'] == 'Car':
            obj['class'] = 'Vehicle'

    # 새로운 json 파일 생성
    file_name = os.path.basename(json_data) # 파일명만 추출
    new_file_path = 'CAM_FRONT/NEW/' + file_name # 저장 경로
    with open(new_file_path, 'w') as new_f:
        json.dump(processed_data, new_f, indent=2)

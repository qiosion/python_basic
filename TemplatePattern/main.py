# 같은 폴더 내의 파일 이름(모듈 명)을 작성하여, 그 모듈로부터 import 해올 수 있음
from autoVehicle import *
from publicVehicle import *
from Car import *

autoCar = AutoVehicle()
publicCar = PublicVehicle()

autoCar._run()
print("================")
publicCar._run()
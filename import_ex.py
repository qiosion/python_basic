"""
# 모듈을 import 하는 다양한 방식
1. import 파일명
2. from 파일명 import *
3. from 파일명 import 사용할 메서드

ex.1)
import module_ex
print(module_ex.add(1, 2))

ex.3)
from module_ex import add, mul
"""

# ex.2)
from module_ex import *
print(mul(3, 4))
calc = Calc()
print(calc.a + calc.b)

import sympy as sy # as를 이용해 축약어 사용
# x = sy.Symbol('x')
# # (일차방정식) = 0 형태로 만들어서 모두 이항한 후 변수화해줌
# equation = 2 * x - 6
# print(sy.solve(equation))

# 심파이라는 라이브러리부터 특정 메서드만 골라서 임포트
# from sympy import Symbol, solve # 단점 : 임포트한 메서드 만 사용가능
# x = Symbol('x')
# equation = 2 * x - 6
# solve(equation)

# # 방정식 연습
# k = sy.Symbol('k')
# equ1 = k - 6
# sol1 = sy.solve(equ1)
#
# x = sy.Symbol('x')
# equ2 = 2 * x - 10
# sol2 = sy.solve(equ2)
#
# y = sy.Symbol('y')
# equ3 = y / 2 - 8
# sol3 = sy.solve(equ3)
# print(sol1, sol2, sol3)

# # 연립방정식
# x = sy.Symbol('x')
# y = sy.Symbol('y')
#
# equ1 = 3 * x + y - 2
# equ2 = x - 2 * y - 3
#
# sol_dict = sy.solve((equ1, equ2), dict=True)
# print(sol_dict)

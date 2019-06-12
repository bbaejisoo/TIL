# STEP 4 - 연산자

# 1. 이항연산자

# A + B   : A와 B를 더함
# A - B   : A와 B를 뺌
# A * B   : A와 B를 곱함
# A / B   : A와 B를 나눈 몫(실수의 결과)
# A // B   : A와 B를 나눈 정수 몫
# A ** B   : A의 B제곱
# A % B   : A를 B로 나눈 나머지

# 2. 대입연산자

# A += B  => A = A + B
# A -= B  => A = A - B
# A *= B  => A = A * B
# A /= B  => A = A / B
# A //= B  => A = A // B
# A **= B  => A = A ** B
# A %= B  => A = A % B

# ※ / 연산은 나눈 몫을 실수의 결과로 구해주고, // 연산은 정수의 결과로 구해줌에 유의해야 한다.
# 예를 들어, '5 / 2'의 결과는 실수 2.5 이지만, '5 // 2'의 결과는 정수 2이다.

# Example 025
add = 12 + 21
sub = 41 - 22
mul = 2 * 8 
div = 3 / 2
div_int = 3 // 2
exp = 10 ** 3
mod = 34 % 5

print(add)
print(sub)
print(mul)
print(div)
print(div_int)
print(exp)
print(mod)

# Example 026
A, B, C = 1, 2, 3

A += 1
B += A
print(A, B)
A -= 1
C /= B
print(A, B, C)

# PLUS
# 여러 가지 연산자를 동시에 사용할 경우, 연산을 처리하는 순서를 유의해야 한다.
# 연산의 우선순위는 아래와 같다. 위쪽이 우선순위가 높은 연산이다. 익숙해지도록 하자.
# ** : 지수
# ~ + - : 단항 플러스와 마이너스
# * / % // : 곱하기, 나누기, 나머지, 몫
# + - : 덧셈, 뺼셈
# >> << & : 비트 연산자
# <= <> >= : 비교 연산자
# <> == != : 평등 연산자
# += -= 등 : 대입 연산자
# not and : 논리 연산자

# Example 028
X, Y, Z = 3, 7, 21

print(X * Y ** 2)
print((X * Y) ** 2)
print(Z % (X + Y))

# Problem 030
A, B = 3, 7
C = A / B
print(A)
print(B)
print(C)

# Problem 031
A, B, C = 2, 5, 7

A += A + B
B /= A - B
C *= C - B - 2
print(A)
print(B)
print(C)

# PLUS
# 파이썬에서 0x로 시작하는 수는 16진수를, 0o로 시작하는 수는 8진수를 의미한다.
# 예를 들어, 0x13은 10진수로 19를, 0o23은 10진수로 19를 의미한다.
# 파이썬에서는 type() 함수를 활용하여 괄호안 변수의 자료형을 확인할 수 있다.

# Problem 036
print(type(1))
print(type(1.0))




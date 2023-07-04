# STEP 2 - 변수 variable

# 객체지향언어인 파이썬에서 변수는 객체를 가리키는 것이다.
# 객체는 '파이썬에서 사용되는 모든 것'이다.
# 앞으로 나올 정수형 변수, 실수형 변수, 문자열부터 기본 자료구조인 리스트, 튜플 등과 함수, 모듈에 이르기 까지, 모든 것은 객체로 만들어져야한다.

# "a = 3"이라는 파이선 문장은, 3이라는 값을 가지는 정수 타입의 객체를 만들고, a가 그 객체를 가리키도록 한다는 의미이다.
# 따라서 엄밀히 말해서 a는 수학적인 의미의 변수라기보다는 객체를 가리키는 포인터이다.
# 파이썬에서는 "변수명 = 변수에 저장할 값"의 형식으로 변수를 선언한다.

# Example 010
# 변수를 선언할 떄에는 "A = 1"과 같이 수를 할당할 수 도 있지만, "C = A + B"와 같이 다른 변수들의 연산 결과를 저장할 수도 있다.
A = 1
B = 2
C = A + B
print(A)
print(B)
print(C)

# Example 011
# 변수를 선언할 때, 이미 선언된 변수에 덮어씌우는 것도 가능하다.
A = 5
B = A
A = 1
print(A); print(B)
print(A, B)

# Example 012
# 여러 개의 변수를 쉼표를 사용하여 한 줄에 선언할 수가 있다.
# 또한, 실수가 연산에 포함되면 무조건 결과는 실수로 출력된다.
A, B = 1.3, 2
C = A + B
A = A - 0.3
D = 1
print(A, B, C)
print(A + B)
print(C + 1)
print(D + 2.0)

# Problem 013
# 다음 조건을 만족하는 프로그램을 작성하시오.
# 조건
# 1. 변수 x에 2를 저장, 변수 y에 1을 저장한다.
# 2. z를 x와 y의 합으로 저장한다.
# 3. z의 값을 출력한다.
x, y = 2, 1
z = x + y
print(z)

# Problem 014
# 다음 조건을 만족하는 프로그램을 작성하시오.
# 조건
# 1. 변수 A에 2를 저장한다.
# 2. 변수 B에 3을 저장한다.
# 3. 변수는 A, B 두 개만 선언하며, 변수의 재선언을 하지는 않는다.
# 4. print문 안에 변수 A와 B를 모두 사용한다.
# 5. 10을 출력하는 프로그램이다.
A, B = 2, 3
print(A * 2 + B * 2)

# PLUS
# 만약 3.0(실수)를 3(정수)로 바꾸고 싶다면 어떻게 해야할까?
# round()함수를 이용해 주면 된다.
# 즉, A가 3.0일 때, A = round(A)로 A를 재선언하면, A는 3이라는 정수를 가지게 된다.
A = 1.0
print(A)
print(round(A))

A = round(A) # 실수 -> 정수로 재선언
print(A)

# Problem 015
# 식 (20 * 5) + (34 - 2) - 72 / 5 의 계산 결과를 출력하는 프로그램을 작성하시오.
print((20 * 5) + (34 - 2) - 72 / 5)

# Problem 016
a, b, c = 1, 2, 3
print(a * 2 + b + c * 2)
print((a * 2 + b + c * 2) * 10)
print((a * 2 + b + c * 2) * 100)

# Problem 017
A, B = 2.5, 4
C = A * 4 + B
print(C)

# Problem 018
A, B = 1.5, 2
C = A - B
A = A - 0.5
B = B + 1.0
D = 1

print(A)
print(B)
print(C)
print(A + B)
print(C + 0.5)
print(D + 1.0)

# Problem 019
Mon, Tue, Wed = 10000, 24000, 6000
Thu, Fri, Sat = 4000, 31000, 15000
print(Mon)
print(Wed)
print(Fri + Sat)
print(Mon * 1.0)
print(Wed - Thu * 1.0)

# Problem 020
num1, num2, num3 = 10, 20, 30
num1 = num2 = num3
print(num1)
print(num2)
print(num3)

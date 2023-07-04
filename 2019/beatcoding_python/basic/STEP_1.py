# STEP 1 - 출력문 print()

# 파이썬에서는 print()문을 통해 모니터로의 출력을 지원한다.
# 여러가지 사용법이 있으므로 앞으로 나올 example을 통해 익숙해지도록 하자.

# Example 001
# print()문은 괄호 안에 있는 요소를 화면에 출력하는 함수이다.
# 예를 들어, print(5)는 5를 출력한다.
# 아래의 코드를 통해 print()문의 사용법을 익혀보자.
print(2020)
print(4 + 3)
print("Hello")
print('Hello')
print("3" + "A")

# PLUS
# print()문에서 괄호안의 " " 혹은 ' '의 형태는 문자로 인식하고, 따옴표가 없을 겨우 수로 인식한다.
# 따라서 2번째 줄은 4와 3의 더하기 연산의결과를 출력되고, 5번째 줄은 문자 "3"과 "A"를 합하여 "3A라는 문자를 출력한다.

# Example 002
# print(3 + A) : Error => 서로의 자료형이 맞지 않기 때문에, 3과 A는 더할 수 없다. 
# print(Hello) : Error => Hello는 문자열이므로 "Hello"가 되어야한다.
# print(3 + 'Hello') : Error => 문자열과 수를 더할 수 없다.

# Example 003
# print()문은 괄호 안의 요소를 출력한 후 한 줄을 띈다.
# 하지만 end = " "를 활용하면 한 줄을 띄지 않고 출력이 가능하다.
# (만약, end = ' '안에 다른 문자를 넣는다면, 해당하는 문자와 함께 출력문을 마무리한다.)
# 여러 줄의 긴 문자열을 출력하고 싶다면 ''' '''와 같이 따옴표 세개를 함께 사용한다.
# 이 경우, 세 개의 따옴표 안의 문장을 보이는 그대로 출력한다.
print(1);
print(2, end= ' ')
print(3, end= " ")
print(4)
print(5, end= "Finish")
print(6)
print('''This is My
Story for you''')

# Problem 004
# 다음과 같이 1234567890을 출력하는 프로그램을 작성하시오.
print(1234567890)

# Problem 005
# 다음과 같이 자신의 이름을 출력하는 프로그램을 작성하시오.
# "제 이름은 홍길동입니다."
print("제 이름은 홍길동입니다.")

# Problem 006
# 다음 print문의 출력화면을 적으시오.
# Error가 발생 할것 같다면 Error로 작성
print(1234590)
# print(abc) : Error
print(13 - 2)
print(12 + 4 / 2 + 1)
print("A" + "B" + " C")
print("A" + "B")
# print("A" - "B") : Error
# print(52 - "33") : Error

# PLUS
# 나중에 배우겠지만 프로그램의 변수 중에서는 정수와 실수가 있다.
# Problem 006의 "print(12 + 4 / 2 + 1)"에서 
# 12와 4, 2, 1은 모두 정수지만 / 연산은 자동으로 실수영역에서 수행되어진다.
# 그래서 출력이 15가 나오는 것이 아닌 15.0이 출력되는 것이다.

# Problem 007
# 다음과 같은 화면을 출력하는 프로그램을 작성하시오.
# 그대는
# 나에게 왔다가
# 떠나가네...
print('''그대는 
나에게 왔다가
떠나가네...''')

# Problem 008
# 다음과 같은 화면을 출력하시오. (위, 아래 코드는 다르게)
# 23Bc7
# 23Bc7
print("23Bc7")
print("23" + "Bc7")

# Problem 009
print('a')
print('b', 'c', end=' ')
print('D')
print("E", end= "F")
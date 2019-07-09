# STEP 6 - boolean

# boolean은 논리 자료형이다. 즉, 논리적인 식이나 조건이 참인지 거짓인지에 대한 정보를 담을 수 있는 변수이다.
# 따라서 boolean 자료형은 True와 False 두 가지의 값만 가질 수 있으며, 변수의 선언은 다른 변수와 같이 'a = True', 'b = False'와 같은 형식으로 이루어진다.

# Example 049
boolean_1 = True
print(boolean_1)
boolean_2 = False
print(boolean_2)

boolean_3 = 1 > 0
print(boolean_3)

# Example 051
boolean_1 = True & True
boolean_2 = True & False
boolean_3 = False | False
boolean_4 = True | False
boolean_5 = True | True
boolean_6 = True ^ True
boolean_7 = True ^ False

print(boolean_1)
print(boolean_2)
print(boolean_3)
print(boolean_4)
print(boolean_5)
print(boolean_6)
print(boolean_7)

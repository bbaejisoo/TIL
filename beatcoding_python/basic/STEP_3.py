# STEP 3 - 포맷 format

# 여러 변수를 하나의 print()문에서 출력하는 방법에는 여러 가지 방법이 있다.
# 문자열을 여러 가지 출력하기 위해서는 + 연산을 사용할 수 있었다.
# (way1) print("My name is " + name + ". I'm", age, "years old")
# (way2) print("My name is {}. I'm {} years old".format(name, age))

# Example 023
country = "Korea"
population = "50M"
print("{} has about {} people".format(country, population))

# Example 024
num1 = 1.23456789
num2 = 0.22222222
num3 = 1.87654321
num4 = 0.21314151

print("First : {:.2}".format(num1))
print("Second : {:10.4}".format(num2))
print("Third : {}".format(num3))
print("Fourth : {:10.4}".format(num4))
# First : 1.2
# Second :     0.2222
# Third : 1.87654321
# Fourth :     0.2131
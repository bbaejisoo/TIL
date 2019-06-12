# STEP 5 - 비트연산

# SHIFT 연산(>>, <<) : 각 비트를 오른쪽과 왼쪽으로 옮긴다.
# >>1 : 2를 나누는 효과, <<1 : 2를 곱하는 효과
# AND 연산(&) : 각 자릿수를 비교하여 둘 다 1이면 1, 아니면 0을 변환한다.
# OR 연산(|) : 각 자릿수를 비교하여 둘 중 하나만 1이면 1을 변환한다.
# XOR 연산(^) : 각 자릿수를 비교하여 다르면 1, 같으면 0을 변환한다.
# NOT 연산(~) : 1을 0으로, 0은 1으로 변환한다.

# Example 038
a = 0b10110101
b = 0b11011001
c = a + b

print(a, b, c)
print(bin(a & b), a & b)
print(bin(a | b), a | b)
print(bin(a ^ b), a ^ b)
print(bin(a >> 2), a >> 2)
print(bin(a >> 3), a >> 3)
print(bin(a << 2), a << 2)
print(bin(~a), ~a)

# PLUS
# 직관적으로 0b10101010을 ~ 연산자로 연산을 하면 0b01010101을 얻을 것 같다.
# 하지만 실제로 ~ 연산을 적용해보면 -0b10101011(-171)을 얻는다.

# <결과풀이과정>
# 10101010 (170)
# 01010101 (1의 보수)
# 10101010 (다시 1의 보수)
# 10101011 (1을 더하여 2의 보수를 만듦)
# -10101011 (음수 기호 추가, -171)


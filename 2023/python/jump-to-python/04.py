# 홀수, 짝수 판별하기
def is_odd(number):
    if number % 2 == 0:
        return True
    else:
        return False
# Validation
# result = is_odd(0)
# print(result)

# 모든 입력의 평균값 구하기
def avg_number(*args):
    result = 0
    for i in args:
        result +=i
    return result
# print(avg_number(1, 2))
# print(avg_number(1, 2, 3, 4, 5))

# 사용자 입력 저장하기
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')
f.write(user_input)
f.write('\n')
f.close()

# 파일의 문자열 바꾸기
f = open('test.txt', 'r')
body = f.readline()
f.close()
body = f.readline().replace('java', 'python')
f.write(body)
f.close()

# 입력값을 모두 더해 출력하기
import sys
args = sys.argv[1:]
result = 0
for i in args:
    result += int(i)
print(result)
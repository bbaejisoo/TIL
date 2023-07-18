# 정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 return하도록 solution 함수를 완성해주세요.
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 0:
            pass
        else:
            answer.append(i)
    return answer

# 문자열 str1, str2가 매개변수로 주어집니다. str1 안에 str2가 있다면 1을 없다면 2를 return하도록 solution 함수를 완성해주세요.
def solution(str1, str2):
    answer = 0
    if str2 in str1:
        answer += 1
    else:
        answer += 2
    return answer

# 문자열 my_string이 매개변수로 주어질 때, 대문자는 소문자로 소문자는 대문자로 변환한 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(my_string):
    answer = ''
    answer = my_string.swapcase()
    return answer

# 군 전략가 머쓱이는 전쟁 중 적군이 다음과 같은 암호 체계를 사용한다는 것을 알아냈습니다.
# 암호화된 문자열 cipher를 주고받습니다.
# 그 문자열에서 code의 배수 번째 글자만 진짜 암호입니다.
# 문자열 cipher와 정수 code가 매개변수로 주어질 때 해독된 암호 문자열을 return하도록 solution 함수를 완성해주세요.
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher), code):
        answer += cipher[i]
    return answer
# 다른 분들 풀이했던 내용을 보니 엄청 신기하게 하신 분들도 계셨다.
# 전혀 생각 못했다.....
def solution(cipher, code):
    answer = cipher[code-1::code]
    return answer

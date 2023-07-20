# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
        else:
            pass
    return answer

# 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    elif num == 0:
        answer = 'Even'
    else:
        answer = 'Odd'
    return answer

# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
def solution(n):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    n = list(map(int, str(n)))
    for i in range(len(n)):
        answer += n[i]
    return answer

# 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
def solution(arr):
    answer = 0
    for i in arr:
        answer += i / len(arr)
    return answer
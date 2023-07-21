# 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    pcount = s.count('p')
    Pcount = s.count('P')
    ycount = s.count('y')
    Ycount = s.count('Y')
    presult = pcount + Pcount
    yresult = ycount + Ycount
    if presult == yresult:
        answer = True
    else:
        answer = False
    return answer

# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
def solution(n):
    answer = []
    answer = list(map(int, reversed(str(n))))
    return answer

# 문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
# str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
# 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
def solution(s):
    answer = ''
    s = list(map(int, s.split(' ')))
    smin = min(s)
    smax = max(s)
    answer = str(smin) + " " + str(smax)
    return answer

# 

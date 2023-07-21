# 3의 배수의 합 구하기(1~1000까지의 자연수)
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
    i += 1
print(result)

# 별 표시하기
i = 0
while True:
    i += 1
    if i > 5 : break
    print('*' * i)

# 1 부터 100까지 출력하기
for i in range(1, 101):
    print(i)

# 평균 점수 구하기
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in A:
    total += score
average = total // len(A)
print(average)

# 리스트 컴프리헨션 사용하기
# 리스트의 요소 중 홀수만 골라 2를 곱한 값을 result에 담기
numbers = [1, 2, 3, 4, 5]
result = [ n * 2 for n in numbers if n % 2 == 1 ]
print(result)
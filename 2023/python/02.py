## 평균 점수 구하기
jumsu = {'국어':80, '영어':75, '수학': 55}
print((jumsu['국어'] + jumsu['영어'] + jumsu['수학']) / 3)

## 주민등록번호 나누기
pin = "881120-1068234"
yyyymmdd = ''
num = ''
print(pin.split('-')[0])
print(pin.split('-')[1])

## 문자열 바꾸기
a = "a:b:c:d"
b = a.replace(":","#")
print(b)

## 리스트 역순 정렬하기
a = [1, 3, 5, 4, 2]
a.sort()
a.sort(reverse=True)
print(a)

## 리스트를 문자열로 만들기
a = ['Life', 'is', 'too', 'short']
result = ' '.join(a)
print(result)

## 튜플 더하기
a = (1, 2, 3)
a = a + (4, )
print(a)

## 딕셔너리의 값 추출하기
a = {'A':90, 'B':80, 'C': 70}
result = a.pop('B')
print(a)
print(result)

## 리스트에서 중복 제거하기
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
aSet = set(a)
b = list(aSet)
print(b)
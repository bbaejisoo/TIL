# 클래스 상속 받고 메서드 추가하기 1
# 클래스 정의
class Calculator:
    def __init__(self):
        self.value = 0
        
    def add(self, val):
        self.value += val
# minus 추가
class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

# 클래스 상속 받고 메서드 추가하기 2
# 100 이상의 값은 가질 수 없도록
class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)

# 음수 제거하기
sulist = [1, -2, 3, -5, 8, -3]

def posi(x):
    return x > 0

print(list(filter(posi, sulist)))

# 리스트 항목마다 3 곱하여 리턴하기
su = [1, 2, 3, 4]

def gop(val):
    return val * 3

print(list(map(gop, su)))

# 최대값, 최소값
su = [-8, 2, 7, 5, -3, 5, 0, 1]

print(min(su))
print(max(su))

# 디렉터리 이동하고 파일 목록 출력하기
import os
os.chdir("/Users/baejisoo/github/TIL/2023/python/jump-to-python")
os.system("ls")
os.system("ls /Users/baejisoo/github/TIL/2023/python/jump-to-python/")

# 파일 확장자가 .py인 파일만 찾기

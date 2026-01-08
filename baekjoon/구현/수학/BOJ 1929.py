# 첫번째 해결 코드.
## 시간 복잡도 : 3100 ms

import sys

input = sys.stdin.readline

# m 이상 n 이하의 소수 찾기.
def find_prime_nums(num) :
    if num == 1 : return False
    if num == 2 : return True
    for r in range(2, int(num**0.5) + 1):
        if not (num % r) :
            return False
    return True


m, n = map(int, input().split())
for num in range(m, n+1) :
    if find_prime_nums(num):
        print(num)
        


# 두번째 해결 코드 : 짝수 바로 제거, 홀수일 때만 순회 -> 연산량 줄이기
## 시간 복잡도 : 1864 ms
import sys
input = sys.stdin.readline

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

m, n = map(int, input().split())

for num in range(m, n + 1):
    if is_prime(num):
        print(num)

## 1. 리팩토링 전 성공한 코드.
import sys

input = sys.stdin.readline
n = int(input())
answer = 0 
for num in range(1, n+1):
    answer += num
print(answer)

## 2. 리팩토링 코드.

## 2-1. 메서드 사용.
n = int(input())
print(sum(range(1, n + 1)))

## 2-2. 수학 공식 사용.
n = int(input())
print(n * (n + 1) // 2)

## 2-3. 메서드 생성.
def solution():
    n = int(input())
    return n * (n + 1) // 2

print(solution())

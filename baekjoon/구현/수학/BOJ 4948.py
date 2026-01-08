# 첫 번째 통과 코드
## pypy로 통과 python 3 시간 초과 

def is_prime(num):
    if num < 2 : return False
    if num == 2 : return True
    if num % 2 == 0 : return False
    
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0 : return False
    return True

while True :
    n = int(input())
    if n == 0 :
        break
    if n == 1 :
        print(1)
        continue
    answer = 0
    for num in range(n + 1, 2*n ):
        if is_prime(num): answer += 1
    print(answer)
    

# 리팩토링 코드 
## python3 통과 
## 메모리 : 36204, kb 시간 : 1928ms

# 테스트 케이스 저장.
test_cases = []
while True:
    n = int(input())
    
    if n == 0 : break
    test_cases.append(n)

for n in test_cases:
    max_n = 2 * n
    is_prime = [True] * (max_n + 1)
    is_prime[0] = False
    is_prime[1] = True
    
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i + i, max_n + 1, i) :
                is_prime[j] = False

    print(sum(is_prime[n+1:]))
    

# 최종 리팩토링 코드
## 에라토스테네스의 체 한번만 생성하여 사용
## 메모리 : 35824 kb, 시간 : 120ms

import sys
input = sys.stdin.readline

test_cases = []
while True:
    n = int(input())
    if n == 0:
        break
    test_cases.append(n)

max_n = max(test_cases) * 2

is_prime = [True] * (max_n + 1)
is_prime[0] = False
is_prime[1] = True

for i in range(2, int(max_n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i + i, max_n + 1, i):
            is_prime[j] = False

for n in test_cases:
    print(sum(is_prime[n+1:2*n+1]))
import sys

input = sys.stdin.readline

t = int(input())
test_nums = [int(input()) for _ in range(t)]

max_num = max(test_nums)
prime_nums = [True] * (max_num + 1)
prime_nums[0] = prime_nums[1] = False

for num in range(2, max_num+1):
    if prime_nums[num]:
        for next in range(num * num, max_num + 1, num):
            prime_nums[next] = False

primes = [i for i in range(max_num+1) if prime_nums[i]]
    
for test in test_nums:
    l, r = 0, len(primes) - 1
    answer = (0, 0)
    
    while l <= r :
        n, m = primes[l], primes[r]
        if n + m > test:
            r -= 1
            continue
            
        if n + m == test :
            answer = (n, m)
        l +=1 
    
    print(*answer)
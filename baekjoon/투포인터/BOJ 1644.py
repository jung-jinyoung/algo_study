import sys

sys.stdin = open("input.txt", "r")

n = int(input())

def get_primes(n):
    arr = [True] * (n+1)
    arr[0] = arr[1] = False 
    
    for i in range(2, int(n**0.5)+1):
        if arr[i] : 
            # i의 배수들을 모두 제외
            for j in range(i*i, n+1, i) : 
                arr[j] = False
    
    return [i for i in range(2, n+1) if arr[i]]


nums = get_primes(n)
left = 0 
current_sum = 0 
ans = 0 

for right in range(len(nums)):
    current_sum += nums[right]
    
    while current_sum > n :
        current_sum -= nums[left]
        left += 1
        
    if current_sum == n :
        ans +=1
print(ans)
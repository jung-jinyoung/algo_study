n = int(input())
A = 1
arr = list(map(int, input().split()))
for i in range(n):
    A *= arr[i]
    
m = int(input())
B = 1
brr = list(map(int, input().split()))

for j in range(m):
    B *= brr[j]

def gcd(n, m):
    while m != 0:
        n, m = m, n % m
    return n

answer = str(gcd(A, B))
if len(answer) > 9 :
    print(answer[-9:])
else : 
    print(answer)
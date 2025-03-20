import sys

input = sys.stdin.readline

n, x = map(int, input().split())
info = list(map(int, input().split()))

answer = [0,0]

current_sum = 0
for i in range(n):
    current_sum += info[i]
    if i >= x-1 :
        if current_sum > answer[0] :
            answer[0] = current_sum
            answer[1] = 1
        elif current_sum == answer[0]:
            answer[1] +=1
        current_sum -= info[i-x+1]
        continue
    
if (answer[0] > 0):
    print(*answer, sep = "\n")
else :
    print("SAD")
            
            
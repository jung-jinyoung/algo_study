import sys

sys.stdin = open('input.txt','r')

input= sys.stdin.readline
answer =  int(1e9)

def solution(num, cnt): 
    global answer


    if cnt >= answer : 
        return
    if num == 1 and cnt < answer : 
        answer = cnt
        return

    if not (num % 2) :
        solution(num//2,cnt +1 )
    if not (num % 3) :
        solution(num // 3 , cnt + 1)
    solution(num-1,cnt+1) 


N = int(input())

solution(N,0)


print (answer)


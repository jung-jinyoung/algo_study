"""
sys.stdin.readline()에서 줄바꿈 인식되서 에러
-> strip() 으로 해결
"""
import sys

N = int(input())
stack = []

for _ in range(N):
    temp = sys.stdin.readline().strip()
    if temp == "top":
        try : 
            print(stack[-1])
        except IndexError:
            print(-1)
    
    if temp == "size":
        print(len(stack))

    if temp == "empty" and not(len(stack)):
        print(1)
    elif temp == "empty" and len(stack):
        print(0)

    if temp == "pop":
        try :
            print(stack.pop())
        except IndexError:
            print(-1)
        
    if "push" in temp:
        _, num = temp.split()
        stack.append(num)
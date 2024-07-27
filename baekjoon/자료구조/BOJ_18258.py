import sys
from collections import deque

N = int(input())
queue_list =deque()
for _ in range(N):
    temp = sys.stdin.readline().strip()

    if "push" in temp:
        _, num = temp.split()
        queue_list.append(num)

    if "pop" == temp :
        try :
            print(queue_list.popleft())
        except IndexError:
            print(-1)

    if "size" == temp:
        print(len(queue_list))

    if "empty" == temp and not queue_list:
        print(1)
    elif "empty" == temp and queue_list:
        print(0)

    if "front" == temp :
        try :
            print(queue_list[0])
        except IndexError :
            print(-1)

    if "back" == temp:
        try :
            print(queue_list[-1])
        except IndexError:
            print(-1)
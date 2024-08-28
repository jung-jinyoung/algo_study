import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
now = list(map(int,input().strip()))
want = list(map(int,input().strip()))


def change_content(arr,cnt):

    for index in range(1,N):
        if arr[index-1] != want[index-1]:
            for i in range(index-1,index+2):
                if i < N:
                    if arr[i] == 0 :
                        arr[i] = 1
                    else:
                        arr[i] = 0
            cnt+=1
    return cnt



# 0번 째 전구를 켰을 경우

now_on = now[:]
for i in range(2):
    if now_on[i] == 0:
        now_on[i] = 1
    else :
        now_on[i] = 0
# 0번 째 전구를 켜지 않았을 경우
now_off = now[:]


cnt_on = 1
cnt_off = 0

cnt_on = change_content(now_on,1)
cnt_off = change_content(now_off,0)

if now_on != want:
    cnt_on = float('inf')

if now_off != want:
    cnt_off = float('inf')

if cnt_on == float('inf') and cnt_off==float('inf'):
    print(-1)
else:
        print(min(cnt_on, cnt_off))
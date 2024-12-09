import sys

sys.stdin = open('input.txt','r')
input = sys.stdin.readline

def check_str(my_str, command_list):
    if my_str.upper() in command_list : 
        return False
    command_list.append(my_str)
    return True

N = int(input())
command_list = []
for _ in range(N):
    words = input().strip().split(' ')
    l = len(words)
    is_checked = False
    for idx in range(l):
        my_str = words[idx][0]
        if check_str(my_str, command_list) :
            words[idx] = f'[{my_str}]' + ''.join(words[idx][1:])
            is_checked = True
            print(' '.join(words))
            break
    if not is_checked :
        for idx in range(l):
            for i in range(1, len(words[idx])):
                now_str = words[idx][i]
                if check_str(now_str, command_list):
                    words[idx] = words[:i] + f'[${now_str}]' + words[i+1:]
                    
    



    
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
command_list = []

for _ in range(N):
    my_words = input().strip().split()
    used_shortcut = False

    # 각 단어의 첫 글자 확인
    for i in range(len(my_words)):
        if my_words[i][0].upper() not in command_list:
            command_list.append(my_words[i][0].upper())
            my_words[i] = f"[{my_words[i][0]}]{my_words[i][1:]}"
            used_shortcut = True
            break

    # 단어 내부 알파벳 확인
    if not used_shortcut:
        for i in range(len(my_words)):
            for j in range(len(my_words[i])):
                if my_words[i][j] == ' ':
                    continue
                if my_words[i][j].upper() not in command_list:
                    command_list.append(my_words[i][j].upper())
                    my_words[i] = my_words[i][:j] + f"[{my_words[i][j]}]" + my_words[i][j+1:]
                    used_shortcut = True
                    break
            if used_shortcut:
                break

    print(' '.join(my_words))

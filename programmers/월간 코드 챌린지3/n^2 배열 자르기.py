"""
n 행들을 붙여서 1차원 리스트로 만들 때의 규칙 찾기
"""
def solution(n, left, right):
    answer = []
    
    for turn in range(left,right+1):
        a, b = divmod(turn,n)
        num = a+1
        if b <= a :
            answer.append(num)
        else:
            answer.append(b+1)
    
    return answer
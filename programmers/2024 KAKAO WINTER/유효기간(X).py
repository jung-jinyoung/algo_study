"""

20 개 중 8개 맞음

"""

def solution(today, terms, privacies):
    # 오늘 날짜 정수형으로 변환
    year, month, days = map(int, today.split('.'))

    # 정보 딕셔너리로 저장
    terms_dict = {}
    for term in terms:
        s, n = term.split()
        terms_dict[s] = int(n)

    check_list = []
    for check_info in privacies:

        # 가입한 날과 이용약관 확인
        y, m, d = map(int, check_info[:-2].split("."))
        term = check_info[-1]

        m += terms_dict[term]
        if m > 12:
            y += 1
            m -= 12

        d -= 1
        if d == 0:
            d = 28
            m -= 1

        check_list.append([y, m, d])

    answer = []
    print(check_list)
    for idx in range(len(privacies)):
        check_term = check_list[idx]
        if year > check_term[0]:
            answer.append(idx + 1)
            continue
        if year == check_term[0]:
            if month > check_term[1]:
                answer.append(idx + 1)
                continue
            if month == check_term[1]:
                if days > check_term[2]:
                    answer.append(idx + 1)

    return answer

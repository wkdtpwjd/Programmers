def solution(d,budget):
    d.sort()
    answer = 0

    for i in d:
        if i > budget:
            break
        budget -= i
        answer += 1

    return answer

def solution(people,limit):
    people.sort()
    answer = 0
    # 최소한의 보트개수를 세려면 가장무거운사람+가장가변운사람 이런식으로 묶어야함
    i ,j = 0,len(people)-1

    while i<=j:
        if people[i] + people[j] <= limit:
            i += 1
        j -=1
        answer += 1
    return answer


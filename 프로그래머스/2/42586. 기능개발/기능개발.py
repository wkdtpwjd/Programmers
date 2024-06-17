def solution(progresses,speeds):
    answer = []
    x = 0
    day = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] == 0:
            x = (100-progresses[i])//speeds[i]
        else:
            x = (100-progresses[i])//speeds[i] + 1
        day.append(x)
    stack = [day[0]]
    cnt = 1


    for i in range(1,len(day)):
        if day[i] > stack[-1]:
            answer.append(cnt)
            stack[-1] = day[i]
            cnt = 1
        else:
            cnt+=1

    answer.append(cnt)
    return answer

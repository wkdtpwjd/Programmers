def solution(priorities,location):
    q = []
    answer = 0
    for idx,pri in enumerate(priorities):
        q.append((idx,pri))
    while q:
        max_v = max(q,key=lambda x:x[1])[1]
        t =q.pop(0)
        if t[1] < max_v:
            q.append(t)
        else:
            answer+= 1
            if t[0] == location:
                return answer

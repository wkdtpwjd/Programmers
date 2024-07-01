from itertools import permutations
def solution(k,dungeons):
    arr = []
    dungeons = permutations(dungeons)
    for i in dungeons:
        cnt = 0
        a = k
        for j in i:
            if a>= j[0]:
                cnt += 1
                a -= j[1]
            else:
                arr.append(cnt)
                break
        else:
            arr.append(cnt)
    return max(arr)
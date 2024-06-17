import itertools

def solution(k,dungeons):
    initial = k
    arr = [] # 각 순열의 순서에 맞게 참가했을떄 참가할 수 있는 던전수 담는 리스트
    perms = itertools.permutations(dungeons)
    for p in perms:
        cnt = 0
        for d in p:
            if d[0] <= k:
                k -= d[1]
                cnt += 1
            else:
                break
        arr.append(cnt)
        k = initial
    return max(arr)
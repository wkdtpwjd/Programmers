import heapq

def solution(scoville,K):
    cnt = 0
    scoville.sort()
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        min_v1 = heapq.heappop(scoville)
        if min_v1 >= K :
            return cnt
        min_v2 = heapq.heappop(scoville)
        heapq.heappush(scoville,min_v1+(min_v2*2))
        cnt += 1

    if scoville[0] >= K:
        return cnt
    else:
        return -1

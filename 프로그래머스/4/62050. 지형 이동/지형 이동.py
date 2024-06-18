import heapq # 최소비용찾는거니까 힙큐사용하기

di = [-1,0,1,0]
dj = [0,1,0,-1]

def solution(land,height):
    total_cost = 0
    n = len(land)
    visited = [[False] * n for _ in range(n)]
    heap = [(0,0,0)] # 최소비용이니까 비용이 첫번재 요소로 가도록(비용,시작좌표)
    while heap:
        current_cost,i,j = heapq.heappop(heap)
        if not visited[i][j]:
            visited[i][j] = True
            total_cost += current_cost
            for d in range(4):
                ni = i +di[d]
                nj = j +dj[d]
                if 0<=ni<n and 0<=nj<n :
                    tem_cost = abs(land[i][j]-land[ni][nj])
                    if tem_cost <= height:
                        new_cost = 0
                    else:
                        new_cost = tem_cost
                    heapq.heappush(heap,[new_cost,ni,nj])

    return total_cost

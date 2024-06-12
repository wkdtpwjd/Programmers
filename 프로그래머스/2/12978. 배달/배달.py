import heapq
def solution(N, road, K):
    answer = 0
    # 다익스트라 (최소비용) costs 만들어서 푸는것
    # 연결정보만들기
    graph = {}
    for a,b,c in road:
        if a not in graph:
            graph[a] = [(c,b)]
        else:
            graph[a].append((c,b))
        if b not in graph:
            graph[b] = [(c,a)]
        else:
            graph[b].append((c,a))
    # return graph {1: [(1, 2), (2, 4)], 2: [(1, 1), (3, 3), (2, 5)],
    times = {node:float('infinity') for node in graph}
    times[1] = 0
    min_heap = [(0,1)] # 현재 시간과 현재 마을
    while min_heap:
        current_time,current_node = heapq.heappop(min_heap)
        if times[current_node] < current_time:
            continue
        for new_time,nei in graph[current_node]:
            time = new_time + current_time
            if time < times[nei]:
                times[nei] = time
                heapq.heappush(min_heap,(time,nei))
    # return times {1: 0, 2: 1, 3: 4, 5: 3, 4: 2}
    for i in times:
        if times[i] <= K:
            answer += 1
    return answer


import heapq

def solution(n,costs):
    # 그래프 생성하기
    graph = {} #키가 노드고 값이(비용,노드)
    for a,b,c in costs:
        if a not in graph:
            graph[a] = [(c,b)]
        elif a in graph :
            graph[a].append((c,b))
        if b not in graph:
            graph[b] = [(c,a)]
        elif b in graph:
            graph[b].append((c,a))
    connected = set()
    total_cost = 0
    min_heap = [(0,0)] #  현재 비용과 노드번호
    while min_heap and len(connected) < n:
        cost,node = heapq.heappop(min_heap)
        if node in connected:
            continue
        connected.add(node)
        total_cost += cost
        for new_cost,nei in graph[node]:
            if nei not in connected:
                heapq.heappush(min_heap,(new_cost,nei))
    return total_cost


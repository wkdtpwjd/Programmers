def solution(k,tangerine):
    graph = {}
    for i in tangerine:
        if i not in graph:
            graph[i] = 1
        else:
            graph[i] += 1
    graph = sorted(graph.items(),key=lambda x:x[1],reverse=True)
    # 각 크기별 몇개인지 세서 개수가 가장많은것 순으로 정렬
    type = 0 # 종류의 수
    cnt = 0 # 현재까지 귤의 수

    for i in graph:
        cnt += i[1]
        type += 1
        if cnt >= k:
            return type


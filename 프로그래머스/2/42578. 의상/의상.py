def solution(clothes):
    graph = {}
    for i in clothes:
        if i[1] not in graph:
            graph[i[1]] = 1
        else:
            graph[i[1]] += 1
    answer = 1
    for i in graph.items() :
        answer *= i[1]+1
    return answer-1
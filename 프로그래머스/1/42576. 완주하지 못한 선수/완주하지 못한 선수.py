def solution(participant,completion):
    graph = {}
    for i in participant:
        if i not in graph:
            graph[i] = 1
        else:
            graph[i] += 1
    for i in completion:
        graph[i] -= 1

    for i in graph.items():
        if i[1] != 0:
            return i[0]
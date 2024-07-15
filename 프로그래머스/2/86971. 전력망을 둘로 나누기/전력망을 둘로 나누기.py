def solution(n,wires):
    def dfs(start,ignore):
        cnt = 0
        visited = [0] * (n+1)
        stack = [start]
        visited[start] = 1
        while stack:
            t = stack[-1]
            for i in graph[t]:
                if i == ignore:
                    continue
                if visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
                    cnt += 1
                    break
            else:
                stack.pop()
        return cnt


    graph = {} # 전력망연결정보를 나타내는 그래프
    for i in wires:
        if i[0] not in graph:
            graph[i[0]] = [i[1]]
        else:
            graph[i[0]].append(i[1])
        if i[1] not in graph:
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]].append(i[0])

    diff = [] # wires배열의 처음부터 전력망을 끊었을때 송전탑개수의 차이를 담을배열
    for i in wires:
        diff.append(abs(dfs(i[0],i[1])-dfs(i[1],i[0])))
    return min(diff)
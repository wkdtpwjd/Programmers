def solution(n,wires):
    def dfs(a,b): # a 에서 시작해서 송전탑 개수세는 함수
        cnt = 1
        stack = [a]
        visited = [0] * n
        visited[a-1] = 1
        while stack:
            t = stack[-1]
            for i in graph[t]:
                if i == b: # 연결을끊는것이므로 볼필요없음
                    continue
                if visited[i-1] == 0:
                    stack.append(i)
                    visited[i-1] = 1
                    cnt += 1
                    break
            else:
                stack.pop()

        return cnt
    graph = {}
    for s,e in wires:
        if s not in graph:
            graph[s] = [e]
        else:
            graph[s].append(e)
        if e not in graph:
            graph[e] = [s]
        else:
            graph[e].append(s)
    # return graph {1: [2], 2: [1, 3], 3: [2, 4], 4: [3]}

    diff = [] # 각 송전탑의 차이를 넣을 배열
    # wires를 돌면서 하나씩 포문을 돌면서 차이를 배열에 담는다
    for wire in wires:
        diff.append(abs(dfs(wire[0],wire[1])-dfs(wire[1],wire[0])))

    return min(diff)


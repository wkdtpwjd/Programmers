def solution(n,wires):
    def dfs(start,ignore):
        visited = [0] * (n+1)
        cnt = 1
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

    graph = {}
    # 연결정보 만들기
    for a,b in wires:
        if a not in graph:
            graph[a] = [b]
        else:
            graph[a].append(b)
        if b not in graph:
            graph[b] = [a]
        else:
            graph[b].append(a)
    diff = []
    for a,b in wires:
        diff.append(abs(dfs(a,b)-dfs(b,a)))
    return min(diff)






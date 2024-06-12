def solution(n,computers):
    def dfs(start):
        stack = [start]
        visited[start] = 1
        while stack:
            t = stack[-1]
            for k in range(n):
                if k == t:
                    continue
                if computers[t][k] == 1 and visited[k] == 0:
                    stack.append(k)
                    visited[k] = 1
                    break
            else:
                stack.pop()

    net_cnt = 0 # 답이될 네트워크개수
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            net_cnt += 1
            dfs(i)
    return net_cnt
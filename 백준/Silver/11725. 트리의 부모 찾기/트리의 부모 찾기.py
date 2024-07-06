def dfs(start):
    stack = [start]
    visited[start] = 1
    while stack:
        t = stack.pop()
        for i in adj[t]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1
                answer[i] = t
    return answer


n = int(input()) #노드의 개수
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = [0] * (n+1)  # 각 인덱스가 노드번호고 값이 부모노드번호인 배열
for _ in range(n-1):
    a,b = map(int,input().split())  # 트리의 연결정보
    adj[a].append(b)
    adj[b].append(a)
# 루트노드는 1번
dfs(1)
for i in range(2,len(answer)):
    print(answer[i])
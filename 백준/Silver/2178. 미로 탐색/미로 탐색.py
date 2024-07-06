def bfs(x,y):
    queue = [(x,y)]
    visited[x][y] = 1
    while queue:
        a,b= queue.pop(0)
        if  a == n-1 and b == m-1:
            return visited[a][b]
        for d in range(4):
            ni = a + di[d]
            nj = b + dj[d]
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and miro[ni][nj]:
                queue.append((ni,nj))
                visited[ni][nj] = visited[a][b] + 1


di = [-1,0,1,0]
dj = [0,1,0,-1]
n , m = map(int,input().split())
miro = [list(map(int,input())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

print(bfs(0,0))
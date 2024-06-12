di = [-1,0,1,0]
dj = [0,1,0,-1]

def solution(maps):
    n,m = len(maps),len(maps[0])
    def bfs(start,end):
        visited = [[False]*m for _ in range(n)]
        queue = [(start,end,1)]
        visited[start][end] = True
        while queue:
            x,y,answer = queue.pop(0)
            if x == n-1 and y == m-1:
                return answer
            for d in range(4):
                nx = x + di[d]
                ny = y + dj[d]
                if 0<= nx < n and 0<= ny < m and maps[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx,ny,answer+1))
                    visited[nx][ny] = True
        return -1

    return bfs(0,0)
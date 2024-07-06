from collections import deque


di = [-1,0,1,0]
dj = [0,1,0,-1]
n,k = map(int,input().split()) #  =n*n 배열이고  1부터 k까지 바이러스 있음
arr = [list(map(int,input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
s,find_x,find_y= map(int,input().split())


# 일단 배열에서 0이 아닌 지점을 찾아서 담을 배열
lst = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 :
            lst.append((arr[i][j],i,j,0))
lst.sort(key=lambda x:x[0])  # 바이러스의 숫자를 기준으로 오름차순(낮은숫자부터 전염되므로)
# [(1, 0, 0), (2, 0, 2), (3, 2, 0)]
q = deque(lst)

while q:
    num,x,y,second = q.popleft()
    if second == s:
        break
    for d in range(4):
        nx = x + di[d]
        ny = y + dj[d]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
            arr[nx][ny] = num
            q.append((num,nx,ny,second+1))
print(arr[find_x-1][find_y-1])
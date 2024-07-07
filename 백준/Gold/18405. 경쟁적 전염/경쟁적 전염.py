n,k = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
s,x,y = map(int,input().split())

di = [-1,0,1,0]
dj = [0,1,0,-1]



q = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0 :
            q.append((arr[i][j],i,j,0))
q.sort()

while q:
    virus_num,r,l,second = q.pop(0)
    if second == s:
        break
    for d in range(4):
        nr = r + di[d]
        nl = l + dj[d]
        if 0<=nr<n and 0<=nl<n and arr[nr][nl] == 0:
            arr[nr][nl] = virus_num
            q.append((virus_num,nr,nl,second+1))

print(arr[x-1][y-1])
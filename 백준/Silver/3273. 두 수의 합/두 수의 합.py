n = int(input())
arr = list(map(int,input().split()))
x = int(input())

answer = 0
arr.sort()
l,r = 0,len(arr)-1
while l<r:
    temp = arr[l]+arr[r]
    if temp == x:
        answer += 1
        r-= 1
    elif temp < x:
        l += 1
    else:
        r -= 1
print(answer)
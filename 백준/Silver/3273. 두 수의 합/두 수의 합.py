N = int(input())
arr = list(map(int,input().split()))
X = int(input())
arr.sort()

left = 0
right = N-1
cnt = 0
while left<right:
    sum_v = arr[left] + arr[right]
    if sum_v > X:
        right -= 1
    elif sum_v < X:
        left += 1
    elif sum_v == X :
        cnt += 1
        left += 1
print(cnt)

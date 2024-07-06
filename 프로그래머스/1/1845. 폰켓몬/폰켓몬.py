def solution(nums):
    arr = []
    for i in nums:
        if len(arr) < len(nums) //2:
            if i not in arr:
                arr.append(i)
    cnt = 0
    for i in arr:
        cnt += 1
    return min(cnt,len(nums)//2)
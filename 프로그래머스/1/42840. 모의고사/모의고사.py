def solution(answer):
    a1 = [1,2,3,4,5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [ 3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    result = []
    arr = []
    for i in range(len(answer)):
        if answer[i] == a1[i%5]:
            cnt1 += 1
        if answer[i] == a2[i % 8]:
            cnt2 += 1
        if answer[i] == a3[i % 10]:
            cnt3 += 1
    arr.append(cnt1)
    arr.append(cnt2)
    arr.append(cnt3)
    max_v = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_v:
            result.append(i+1)
    return result
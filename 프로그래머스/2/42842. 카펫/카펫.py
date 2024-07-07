def solution(brown,yellow):
    area = brown + yellow
    arr = []
    result = []
    for i in range(1,area+1):
        if area % i == 0:
            if i >= area //i:
                arr.append((i,area//i))
    for a,b in arr:  # 가로와 세로
        if (a * 2) + ((b-2) *2) == brown:
            result.append(a)
            result.append(b)
    return result

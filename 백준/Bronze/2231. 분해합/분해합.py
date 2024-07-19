def solution(number):
    for i in range(1,number):
        lst = [int(j) for j in str(i)]
        sum_v = sum(lst)
        if i + sum_v == number:
            return i
    return 0


N = int(input())

print(solution(N))
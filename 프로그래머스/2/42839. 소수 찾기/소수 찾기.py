from itertools import permutations
def sosu(num):
    if num < 2:  # 0 과 1 거르기
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    lst = []
    for i in numbers:
        lst.append(i)  # lst = ['1','7']
    lst2 = []
    for i in range(1,len(numbers)+1):
        arr = permutations(lst,i)
        for k in arr:
            if int(''.join(k)) in lst2:
                continue
            lst2.append(int(''.join(k)))
    # return lst2  # [1, 7, 17, 71]

    for i in lst2:
        if sosu(i) == True:
            answer += 1
    return answer

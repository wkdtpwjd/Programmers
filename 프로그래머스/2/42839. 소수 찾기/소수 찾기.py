from itertools import permutations

def solution(numbers):
    def check(num):
        if num < 2:
            return False
        for i in range(2,num):
            if num % i == 0:
                return False
        return True



    lst = list(numbers)
    arr = []
    answer = 0
    for i in range(1,len(numbers)+1):
        lst2 = permutations(numbers,i)
        for j in lst2:
            if int(''.join(j)) not in arr:
                arr.append(int(''.join(j)))

    for i in arr:
        if check(i) == True:
            answer += 1
    return answer
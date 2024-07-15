from itertools import product
def solution(word):
    cnt = 0
    alpha = ["A","E","I","O","U"]
    dictionary = []
    for i in range(1,6):
        words = product(alpha,repeat=i)
        for j in words:
            dictionary.append(''.join(j))
    dictionary.sort()
    return dictionary.index(word) +1


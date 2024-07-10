from itertools import permutations
t = int(input())
remove_cnt = 0
numbers = ['1','2','3','4','5','6','7','8','9']
lst = list(permutations(numbers,3))

for _ in range(t):
    arr = []
    test,s,b = map(int,input().split())
    test = list(str(test))
    # print(test)  #['1', '2', '3']

    for i in range(len(lst)):
        s_cnt,b_cnt = 0,0
        # print(lst[i])  ('1', '2', '3')

        for j in range(3):
            if test[j] in lst[i]:
                if j == lst[i].index(test[j]):
                    s_cnt += 1
                else:
                    b_cnt += 1
        # print(s_cnt,b_cnt)
        if s_cnt != s or b_cnt != b:
            arr.append(i)
            # print(arr) # 제거할 인덱스집합

    for i in sorted(arr,reverse=True):
        lst.remove(lst[i])
print(len(lst))





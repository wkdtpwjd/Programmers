def f(num):
    arr[num] = -2
    for i in range(n):
        if arr[i] == num:
            f(i)



n = int(input())  # 노드의 개수
arr = list(map(int,input().split())) # 인덱스가 노드번호고 값이 부모노드인 배열
remove_node = int(input())

f(remove_node)
# print(arr)

leaf = 0
for i in range(len(arr)):
    if arr[i] == -2:
        continue
    if i not in arr:
        leaf += 1
print(leaf)
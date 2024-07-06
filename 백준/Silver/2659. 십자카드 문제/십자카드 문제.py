def check(string):  # 스트링을 받아서 정수인 시계수 출력
    # 최소값을 만드니까
    min_v = 0xfffff
    temp = ''
    for i in range(4):
        temp = string[i:]+string[:i]
        if min_v >= int(temp):
            min_v = int(temp)
    return min_v # 시계수 구함


arr = list(map(int,input().split()))
# 시계수 만드는 함수만들기
string_num = ''.join(map(str,arr))
clock_num = check(string_num)

answer = 0
for i in range(1111,clock_num+1):
    if '0' in str(i) :
        continue
    if check(str(i)) == i:
        answer += 1
print(answer)

def solution(jobs):
    answer = 0
    # 소요 시간 오름차순 정렬
    sorted_list = sorted(jobs, key=lambda x: x[1])
    # 리스트가 되어 heappop() 등 heapq 메소드 사용불가능
    # print(sorted_list)
    # [[3, 3], [10, 3], [1, 10]]

    start = 0
    while sorted_list:
        for i in range(len(sorted_list)):
            # 작업 시점이 start보다 크면 pass
            if sorted_list[i][0] <= start:
                start += sorted_list[i][1]
                answer += start - sorted_list[i][0]
                sorted_list.pop(i)
                break
            # 반복문을 모두 돌았을 경우에도!
            # 작업 시점 0초에 투입되는 시간이 없다면 start를 1 증가시켜줘야함
            if i == len(sorted_list) - 1:
                start += 1

    return answer // len(jobs)

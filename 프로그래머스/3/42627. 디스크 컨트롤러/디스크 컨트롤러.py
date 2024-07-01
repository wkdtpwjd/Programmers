def solution(jobs):
    answer = 0
    sorted_list = sorted(jobs,key=lambda x:x[1])

    start = 0
    while sorted_list:
        for i in range(len(sorted_list)):
            if sorted_list[i][0] <= start:
                start += sorted_list[i][1]
                answer += start - sorted_list[i][0]
                sorted_list.pop(i)
                break
            if i == len(sorted_list) -1:
                start += 1
    return answer//len(jobs)

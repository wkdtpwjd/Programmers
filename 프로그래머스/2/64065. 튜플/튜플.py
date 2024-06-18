def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = sorted(s,key=lambda x:len(x))
    for i in s:
        numbers = i.split(',')
        for num in numbers:
            if int(num) not in answer:
                answer.append(int(num))
    return answer

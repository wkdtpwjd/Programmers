def solution(numbers):
    numbers = list(map(str,numbers))
    numbers = sorted(numbers,key=lambda x:x*4,reverse=True)
    answer = ''
    for i in numbers:
        answer += i
    if answer[0] == '0':
        return '0'
    return answer

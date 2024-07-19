def solution(numbers):
    numbers = [str(i) for i in numbers]

    numbers = sorted(numbers,key=lambda x:x*4,reverse=True)
    string = ''.join(numbers)
    if string[0] == '0':
        return '0'
    else:
        return string
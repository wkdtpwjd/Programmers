def solution(bridge_length,weight,truck_weights):
    second = 0
    current_w = 0
    queue = [0] * bridge_length

    while truck_weights:
        second += 1
        current_w -= queue.pop(0)
        if current_w + truck_weights[0] <= weight:
            queue.append(truck_weights[0])
            current_w += truck_weights.pop(0)
        else:
            queue.append(0)

    second += len(queue) # 마지막 트럭이 들어가면 나올때까지 시간더해주기
    return second
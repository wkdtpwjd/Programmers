def solution(bridge_length,weight,truck_weights):
    q = [0] * bridge_length
    current_w = 0
    second = 0
    while truck_weights:
        second += 1
        current_w -= q.pop(0)
        if current_w + truck_weights[0] <= weight:
            q.append(truck_weights[0])
            current_w += truck_weights.pop(0)
        else:
            q.append(0)

    second += bridge_length
    return second
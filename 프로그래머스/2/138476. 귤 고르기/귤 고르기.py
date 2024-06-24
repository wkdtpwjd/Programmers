def solution(k, tangerine):
    from collections import Counter
    
    tangerine_counts = Counter(tangerine)
    sorted_counts = sorted(tangerine_counts.values(), reverse=True)
    
    cnt = 0
    for count in sorted_counts:
        k -= count
        cnt += 1
        if k <= 0:
            break
    return cnt


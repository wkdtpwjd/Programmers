def solution(n, money):
    # dp 배열 초기화, 0부터 n까지 저장
    dp = [0] * (n + 1)
    dp[0] = 1  # 0원을 만드는 방법은 1가지

    # 각 동전에 대해서
    for coin in money:
        # dp 배열을 업데이트
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]

    return dp[n]

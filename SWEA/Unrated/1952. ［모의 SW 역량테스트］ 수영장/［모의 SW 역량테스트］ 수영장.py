T = int(input())
for t in range(T):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    dp = [0] * 13 # 1~12월 최소 금액들을 저장

    for i in range(1,13):
        # 현재 달의 최소 비용을 계산
        # 이전달 +1일 권 구입 / 이전 달 + 1달 권 / 3달 전에 3달권 구입 중 최소

        dp[i] = min(dp[i-1]+(days[i]*cost[0]), dp[i-1]+cost[1])

        if i >= 3:
            dp[i] = min(dp[i], dp[i-3] + cost[2])

    result = min(dp[12], cost[3])
    print(f'#{t+1} {result}')
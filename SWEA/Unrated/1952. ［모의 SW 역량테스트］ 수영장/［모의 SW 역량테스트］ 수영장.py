# 시작점 : 1월, 누적금액 : 0원

def dfs(month, sum_cost):
    global ans

    if month > 12:
        ans = min(ans, sum_cost)
        return

    # 1일권으로 모두 구매(다음 재귀: 다음 달을 확인)
    dfs(month+1, sum_cost + (days[month]*cost[0]))
    # 1달권 구매(다음 재귀: 다음 달을 확인)
    dfs(month + 1, sum_cost + cost[1])
    # 3달권 구매(다음 재귀: 3달 후를 확인)
    dfs(month + 3, sum_cost + cost[2])
    # 1년권 구매(다음 재귀: 12달 후를 확인)
    dfs(month + 12, sum_cost + cost[3])


T = int(input())
for t in range(T):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    ans = 1e9
    dfs(1, 0)
    print(f'#{t+1} {ans}')

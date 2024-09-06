def solve(cnt, sum_height):
    global ans

    # 기저조건 가지치기. 이미 탑의 높이가 B 이상이라면, 더 이상확인할 필요가 X
    if sum_height >= B:
        ans = min(ans, sum_height)
        return

    if cnt == N:
        return

    # 쌓는다!
    solve(cnt+1, sum_height + arr[cnt])

    # 안 쌓는다!
    solve(cnt + 1, sum_height)




T = int(input())
for t in range(T):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 1e9 # 1억

    solve(0,0)
    print(f'#{t+1} {ans - B}')



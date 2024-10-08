def dfs(i, result):
    global count
    if result == K:
        count += 1
        return
    if i == N:
        return
    dfs(i + 1, result + number[i])
    dfs(i+1, result)
    
T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    number = list(map(int, input().split()))
    count = 0
    dfs(0, 0)
    print(f'#{t} {count}')
def dfs(node,visited):
    visited[node] = 1

    for neighbor in range(1,N+1):
        if friend[node][neighbor] == 1 and visited[neighbor] == 0:
            dfs(neighbor,visited)

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    friend = [[0]*(N+1) for _ in range(N+1)]

    for m in range(M):
        a, b = map(int, input().split())
        friend[a][b] = 1
        friend[b][a] = 1

    visited = [0]*(N+1)

    cnt = 0
    for i in range(1,N+1):
        if visited[i] == 0:

            dfs(i,visited)
            cnt += 1

    print(f'#{t+1} {cnt}')

def dfs(x, y, path):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    if len(path) == 7:
        result.add(path)
        return

    for d in range(4):
        nr = x + dr[d]
        nc = y + dc[d]
        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, path+arr[nr][nc])


T = int(input())
for t in range(T):
    arr = [list(input().split()) for i in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{t+1} {len(result)}')
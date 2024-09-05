def check(row, col):
    # 열
    for i in range(row):
        if visited[i][col] == 1:
            return False

    # 왼쪽 대각선 
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # 오른쪽 대각선 
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def dfs(row):
    global cnt

    if row == N:
        cnt += 1
        return

    for col in range(N):
        if check(row, col):
            visited[row][col] = True
            dfs(row + 1)
            visited[row][col] = False  


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    dfs(0)
    print(f'#{tc} {cnt}')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def dfs(r, c, chance, N, K, A, visited, MAX):
    MAX[0] = max(MAX[0], visited[r][c])
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if not (0 <= nr < N and 0 <= nc < N) or visited[nr][nc]:
            continue
        if A[r][c] > A[nr][nc]:
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance, N, K, A, visited, MAX)
            visited[nr][nc] = 0
        elif chance and A[nr][nc] - K < A[r][c]:
            temp = A[nr][nc]
            A[nr][nc] = A[r][c] - 1
            visited[nr][nc] = visited[r][c] + 1
            dfs(nr, nc, chance-1, N, K, A, visited, MAX)
            visited[nr][nc] = 0
            A[nr][nc] = temp

def solve(N, K, A):
    top = max(map(max, A))
    MAX = [0]
    visited = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if A[i][j] == top:
                visited[i][j] = 1
                dfs(i, j, 1, N, K, A, visited, MAX)
                visited[i][j] = 0

    return MAX[0]

# main
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    result = solve(N, K, A)
    print(f"#{tc+1} {result}")

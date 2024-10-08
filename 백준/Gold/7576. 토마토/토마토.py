from collections import deque


def bfs(lst):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    visited = [[False for _ in range(M)] for _ in range(N)]
    q = deque(lst)

    while q:
        current_tomato = q.popleft()
        for d in range(4):
            nr = current_tomato[0] + dr[d]
            nc = current_tomato[1] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[current_tomato[0]][current_tomato[1]] + 1
                q.append((nr, nc))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
tomatoes = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomatoes.append((i, j))

bfs(tomatoes)

result = 0
is_True = True

for i in arr:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(max(i), result)

print(result-1)

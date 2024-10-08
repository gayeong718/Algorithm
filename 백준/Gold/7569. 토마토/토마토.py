from collections import deque


def bfs(lst):
    dr = [1, -1, 0, 0, 0, 0]
    dc = [0, 0, 1, -1, 0, 0]
    dh = [0, 0, 0, 0, 1, -1]
    q = deque(lst)

    while q:
        current_tomato = q.popleft()
        for d in range(6):
            nh = current_tomato[0] + dh[d]
            nr = current_tomato[1] + dr[d]
            nc = current_tomato[2] + dc[d]
            if 0 <= nr < N and 0 <= nc < M and 0 <= nh < H and arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = arr[current_tomato[0]][current_tomato[1]][current_tomato[2]] + 1
                q.append((nh, nr, nc))


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomatoes = []

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                tomatoes.append((h, i, j))
bfs(tomatoes)

result = 0
for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 0:
                print(-1)
                exit(0)

            result = max(result,arr[h][i][j])

print(result-1)
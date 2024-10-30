from collections import deque

def mark_island(row, col, island_num):
    queue = deque([(row, col)])
    visited[row][col] = 1
    arr[row][col] = island_num
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = island_num
                queue.append((nx, ny))


def bfs(island_num):
    queue = deque()
    dist = [[-1] * N for _ in range(N)]
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == island_num:
                queue.append((i, j))
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()

        for d in range(4):
            nx = x + dr[d]
            ny = y + dc[d]

            if 0 <= nx < N and 0 <= ny < N:
                if arr[nx][ny] > 0 and arr[nx][ny] != island_num:
                    return dist[x][y]
                if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))

    return float('inf')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
min_distance = float('inf')

island_num = 2
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and not visited[i][j]:
            mark_island(i, j, island_num)
            island_num += 1

for num in range(2, island_num):
    min_distance = min(min_distance, bfs(num))

print(min_distance)

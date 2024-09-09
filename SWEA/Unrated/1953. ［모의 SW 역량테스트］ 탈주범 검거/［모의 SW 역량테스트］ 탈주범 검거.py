from collections import deque

# 상 하 좌 우
link = [[],
        [1, 1, 1, 1],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 1, 1, 0],
        [1, 0, 1, 0]]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
rev = [1, 0, 3, 2]


def solve(sr, sc):
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    Q = deque([(sr, sc, 1)])  # (r, c, 거리)

    cnt = 0
    while Q:
        r, c, dist = Q.popleft()
        if dist > L:
            continue
        cnt += 1
        for d in range(4):
            if not link[arr[r][c]][d]:
                continue
            nr = r + dr[d]
            nc = c + dc[d]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if not arr[nr][nc]:
                continue
            if visited[nr][nc]:
                continue
            if link[arr[nr][nc]][rev[d]]:
                visited[nr][nc] = 1
                Q.append((nr, nc, dist + 1))

    return cnt


T = int(input())
for t in range(T):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{t + 1} {solve(R, C)}')

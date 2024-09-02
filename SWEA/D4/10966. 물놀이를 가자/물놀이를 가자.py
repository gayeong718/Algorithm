from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]

    queue = deque()

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'W':
                queue.append((i,j))
                visited[i][j] = 0

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while queue:
        r, c = queue.popleft()
        for d in range(4):
            if dr[d] + r < 0 or dr[d] + r >= N or dc[d] + c < 0 or dc[d] + c >= M:
                continue
            if visited[dr[d]+r][dc[d]+c] != -1:
                continue

            visited[dr[d]+r][dc[d]+c] = visited[r][c] + 1
            queue.append((dr[d]+r, dc[d]+c))


    result = 0
    for i in range(N):
        for j in range(M):
            result += visited[i][j]


    print(f'#{t+1} {result}')

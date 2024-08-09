def dfs(r,c,visited):

    if maze[r][c] == 3:
        return 1

    dr = [1,-1,0,0]
    dc = [0,0,1,-1]



    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if (0 <= nr < 16 and 0 <= nc < 16) and visited[nr][nc] == 0 and maze[nr][nc] != 1:
            visited[nr][nc] = 1
            if dfs(nr, nc, visited):
                return 1
    return 0


def start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                visited[i][j] = 1
                return dfs(i, j,visited)

for t in range(10):
    T = int(input())
    maze = [list(map(int,input().strip())) for _ in range(16)]
    visited = [[0]*16 for i in range(16)]

    reuslt = start()
    print(f'#{T} {reuslt}')
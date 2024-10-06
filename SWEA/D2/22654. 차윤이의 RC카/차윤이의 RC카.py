
def solve(s, cmd):
    path = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    current_path = 0
    x, y = s

    for c in range(len(cmd)):
        if cmd[c] == 'A':
            dx, dy = path[current_path]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 'T':
                x, y = nx, ny
        elif cmd[c] == 'R':
            current_path = (current_path + 1) % 4
        elif cmd[c] == 'L':
            current_path = (current_path - 1) % 4

    return (x, y)


T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    Q = int(input())
    command = [list(input().split()) for _ in range(Q)]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start_point = (i, j)
            elif arr[i][j] == 'Y':
                end_point = (i, j)

    result_lst = []

    for q in range(Q):
        num_command = int(command[q][0])
        cmd = list(command[q][1])

        final_position = solve(start_point, cmd)

        if final_position == end_point:
            result_lst.append("1")
        else:
            result_lst.append("0")

    result = ' '.join(result_lst)
    print(f'#{t + 1} {result}')

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * (N*N + 1)

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(N):
        for j in range(N):
            for d in range(4):
                if 0 <= i+dr[d] < N and 0 <= j+dc[d] < N:
                    if arr[i+dr[d]][j+dc[d]] == arr[i][j] + 1:
                        check[arr[i][j]] = 1
                        # 이미 체크된 순간, 다른 방향은 볼 필요가 없음
                        # 동일한 숫자가 없으니
                        break

    cnt = 0
    max_cnt = 0
    start = 0 # cnt : 하나씩 체크, max_cnt:정답, start : 계산을 시작할 위치
    for i in range(N*N-1, -1, -1):
        if check[i] == 1:
            cnt += 1
        else:
            if max_cnt <= cnt:
                max_cnt = cnt
                start = i + 1

            cnt = 0
    print(f'#{t+1} {start} {max_cnt+1}')


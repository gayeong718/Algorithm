T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x: x[1])

    cnt = 0
    current_e = 0

    while arr:

        start, end = arr.pop(0)

        if start >= current_e:
            cnt += 1
            current_e = end
        else:
            continue


    print(f'#{t+1} {cnt}')

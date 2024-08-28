def solve(cnt,used,start):
    global min_val
 
    if cnt == N//2:
        sum_a = 0
        sum_b = 0
        for i in range(N):
            for j in range(i+1,N):
                if used[i] == 1 and used[j] == 1:
                    sum_a += arr[i][j] + arr[j][i]
 
                elif used[i] == 0 and used[j] == 0:
                    sum_b += arr[i][j] + arr[j][i]
 
        min_val = min(min_val, abs(sum_a - sum_b))
        return
 
    for i in range(start, N):
        if used[i] == 0:
            used[i] = 1
            solve(cnt+1, used, i+1)
            used[i] = 0
 
 
 
 
T = int(input())
for t in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for i in range(N)]
    used = [0]*N
    min_val = float('inf')
 
    solve(0,used,0)
    print(f'#{t} {min_val}')
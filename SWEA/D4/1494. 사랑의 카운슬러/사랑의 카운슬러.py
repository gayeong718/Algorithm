def love_matching(lst=[], idx=0):

    if len(lst) == N//2:
        global min_value

        vector_sum = [0, 0]

        for i in range(N):
            if i in lst:
                for j in range(2):
                    vector_sum[j] += arr[i][j]
            else:
                for j in range(2):
                    vector_sum[j] -= arr[i][j]

        result = vector_sum[0]**2 + vector_sum[1]**2
        min_value = min(min_value, result)



        return


    for i in range(idx, N):
        if i in lst:
            continue
        lst.append(i)
        love_matching(lst, i+1)
        lst.pop()


T = int(input())

for t in range(T):
    N = int(input())
    arr = []
    min_value = float('inf')
    for i in range(N):
        arr.append(list(map(int, input().split())))

    love_matching()
    print(f'#{t+1} {min_value}')
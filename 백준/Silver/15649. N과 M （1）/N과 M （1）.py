def back():
    # 종료조건
    if len(result_list) == M:
        print(' '.join(map(str, result_list)))
        return

    for i in range(1,N+1):
        if used[i] == 0:
            result_list.append(i)
            used[i] = 1

            back()
            result_list.pop()
            used[i] = 0





N, M = map(int,input().split())

result_list = []
used = [0]*(N+1)
back()

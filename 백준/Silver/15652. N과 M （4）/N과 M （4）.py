def back(start):
    if len(result_list) == M:
        print(' '.join(map(str, result_list)))
        return

    for i in range(start, N + 1):
        result_list.append(i)
        back(i)
        result_list.pop()

N, M = map(int, input().split())
result_list = []
back(1)
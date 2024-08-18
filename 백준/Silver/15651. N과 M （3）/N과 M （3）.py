def back():

    if len(result_list) == M:
        print(' '.join(map(str,result_list)))
        return

    for i in arr:
        result_list.append(i)
        back()
        result_list.pop()
    pass


N, M = map(int, input().split())
result_list = []
arr = [i+1 for i in range(N)]
back()
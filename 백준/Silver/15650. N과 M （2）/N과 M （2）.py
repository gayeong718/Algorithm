def back(start):

    if len(result_list) == M:
        print(' '.join(map(str,result_list)))

    for i in range(start,N):
        result_list.append(arr[i])
        back(i+1)
        result_list.pop()


N, M = map(int,input().split())
arr = [i+1 for i in range(N)]
result_list = []
back(0)
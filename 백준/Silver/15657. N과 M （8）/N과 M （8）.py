def solve(start):

    if len(result_list) == M:
        print(' '.join(map(str, result_list)))
        return

    for i in range(start,N):
        result_list.append(arr[i])
        solve(i)
        result_list.pop()




N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result_list = []

solve(0)
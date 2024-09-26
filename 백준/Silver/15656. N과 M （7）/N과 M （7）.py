def solve():

    if len(result_list) == M:
        print(' '.join(map(str, result_list)))
        return

    for i in arr:
        result_list.append(i)
        solve()
        result_list.pop()




N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result_list = []

solve()
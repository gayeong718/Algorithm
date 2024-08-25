def back(start):

    if len(result_list) == M:
        print(' '.join(map(str, result_list)))
        return

    for i in range(start, len(arr)):
        if used[arr[i]] == 0:
            result_list.append(arr[i])
            used[arr[i]] = 1
            back(i+1)
            result_list.pop()
            used[arr[i]] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result_list = []
used = {}
for i in arr:
    used[i] = 0

back(0)
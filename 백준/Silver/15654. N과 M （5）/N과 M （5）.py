def back():

    if len(result_list) == M:
        print(' '.join(map(str,result_list)))

    for i in arr:
        if used[i] == 0:
            result_list.append(i)
            used[i] = 1
            back()
            result_list.pop()
            used[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
result_list = []
used = {}
for i in arr:
    used[i] = 0

back()
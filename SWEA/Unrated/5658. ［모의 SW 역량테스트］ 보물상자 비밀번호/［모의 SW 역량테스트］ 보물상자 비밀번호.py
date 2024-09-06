T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    arr = list(input())


    num_len = N // 4
    nums = []
    for mix in range(num_len):
        for i in range(0, N-num_len+1, num_len):
            num = arr[i]
            for j in range(num_len-1):
                num += arr[i+j+1]

            nums.append(num)


        poped_num = arr.pop()
        arr.reverse()
        arr.append(poped_num)
        arr.reverse()
    # 중복제거
    nums_set = set(nums)
    nums = [int(num, 16) for num in nums_set]
    sorted_nums = sorted(nums,reverse=True)

    print(f'#{t+1} {sorted_nums[K-1]}')


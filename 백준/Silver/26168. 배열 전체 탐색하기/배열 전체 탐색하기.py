N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(M):
    rule_list = list(map(int, input().split()))
    if rule_list[0] == 1:
        result_list = []

        for i in nums:
            if i >= rule_list[1]:
                result_list.append(i)
        print(len(result_list))

    if rule_list[0] == 2:
        result_list = []

        for i in nums:
            if i > rule_list[1]:
                result_list.append(i)
        print(len(result_list))

    if rule_list[0] == 3:
        result_list = []
        for i in nums:
            if rule_list[1] <= i <= rule_list[2]:
                result_list.append(i)


        print(len(result_list))
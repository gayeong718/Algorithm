N = int(input().strip())
money_list = [int(input().strip()) for _ in range(N)]

money_list.sort(reverse=True)
max_money = []

for i in range(len(money_list)):
    calculated_value = money_list[i] - i
    if calculated_value > 0:
        max_money.append(calculated_value)

print(sum(max_money))
N, M = map(int, input().split())
card_list = list(map(int,input().split()))
sum_cards_list = []

for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum_cards = card_list[i]+card_list [j]+card_list [k] 
            sum_cards_list.append(sum_cards)

find_max=[]
for max_num in sum_cards_list:
    if M - max_num >=0:
        find_max.append(max_num)
    else:
        continue

print(max(find_max))
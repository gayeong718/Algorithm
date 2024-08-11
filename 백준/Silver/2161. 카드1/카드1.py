def card(queue, poped_card):
    if len(queue) == 1:
        result_list = poped_card
        result_list.append(queue[0])
        return ' '.join(map(str,result_list))


    poped_card.append(queue.popleft())
    queue.append(queue.popleft())
    return card(queue,poped_card)




from collections import deque
N = int(input())
queue = deque(i+1 for i in range(N))
poped_card = []
print(card(queue,poped_card))
N = int(input())
stack = []

for i in range(N):
    order = input().split()

    if order[0] == 'push':
        stack.append(order[1])

    if order[0] == 'pop':
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)

    if order[0] == 'size':
        print(len(stack))

    if order[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    if order[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            pop_num = stack.pop()
            stack.append(pop_num)
            print(pop_num)


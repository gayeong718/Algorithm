N = int(input())

list_xy = []
for n in range(N):
    X,Y = map(int, input().split())
    for x in range(X,X+10):
        for y in range(Y,Y+10):
            list_xy.append((x,y))

list_xy = set(list_xy)
print(len(list_xy))

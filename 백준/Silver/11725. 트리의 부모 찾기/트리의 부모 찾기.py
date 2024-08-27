from collections import deque

N = int(input())
tree = [[] for i in range(N+1)]
parent = [0]*(N+1)
for n in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


parent[1] = 0
q = deque()
q.append(1)

while q:
    current = q.popleft()
    for i in tree[current]:
        if parent[i] == 0:
            parent[i] = current
            q.append(i)



print(*parent[2:],sep="\n")
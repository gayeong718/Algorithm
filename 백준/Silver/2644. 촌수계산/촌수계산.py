from collections import deque


def bfs(start):
    q = deque()
    visited = [False for _ in range(N + 1)]

    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()

        for i in family[current]:
            if not visited[i]:
                visited[i] = True
                result[i] = result[current] + 1
                q.append(i)


N = int(input())
a, b = map(int, input().split())
M = int(input())
family = [[] for _ in range(N + 1)]
result = [0 for _ in range(N + 1)]
for m in range(M):
    x, y = map(int, input().split())
    family[x].append(y)
    family[y].append(x)

bfs(a)
if result[b] != 0:
    print(result[b])
else:
    print(-1)
E = int(input())
V = int(input())

adj = [[0]*(E+1) for _ in range(E+1)]

for _ in range(V):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(s):
    stack = [s]
    visited = [False] * (E+1)
    visited[s] = True
    count = 0

    while stack:
        current = stack.pop()
        count += 1

        for i in range(1, E+1):
            if adj[current][i] == 1 and not visited[i]:
                stack.append(i)
                visited[i] = True

    return count - 1  # 시작 노드는 제외

print(dfs(1))
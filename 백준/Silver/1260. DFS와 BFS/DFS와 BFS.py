from collections import deque

# 그래프의 정점, 간선, 시작 정점 입력 받기
N, M, V = map(int, input().split())

adj = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a][b] = 1
    adj[b][a] = 1

def dfs(start):
    stack = [start]
    visited = [False] * (N + 1)
    result = []

    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            result.append(node)
            # 인접 노드를 내림차순으로 스택에 추가 (그래야 오름차순 방문)
            for i in range(N, 0, -1):
                if adj[node][i] == 1 and not visited[i]:
                    stack.append(i)

    return ' '.join(map(str, result))

def bfs(start):
    queue = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        # 인접 노드를 오름차순으로 큐에 추가
        for i in range(1, N + 1):
            if adj[node][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

    return ' '.join(map(str, result))

print(dfs(V))
print(bfs(V))
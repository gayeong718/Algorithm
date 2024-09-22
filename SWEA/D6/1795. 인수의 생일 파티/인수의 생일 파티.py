import heapq


def dijkstra(start):
    q = []
    dist = [float('inf')] * (n + 1)
    dist[start] = 0

    heapq.heappush(q, (0, start))

    while q:
        c_dist, c_node = heapq.heappop(q)

        if c_dist > dist[c_node]:
            continue

        for neighbor, weight in graph[c_node]:
            distance = c_dist + weight
            # print(c_dist, weight)
            if dist[neighbor] > distance:
                dist[neighbor] = distance
                heapq.heappush(q, (distance, neighbor))

    return dist


T = int(input())

for t in range(T):
    n, m, x = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))

    dist1 = dijkstra(x)
    # print(dist1)
    max_dist = 0
    for i in range(1, n + 1):
        dist2 = dijkstra(i)
        if i != x:
            max_dist = max(max_dist, dist1[i] + dist2[x])

    print(f'#{t+1} {max_dist}')
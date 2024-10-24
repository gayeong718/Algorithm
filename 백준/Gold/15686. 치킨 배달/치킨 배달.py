from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
home = []
chicken = []
result = 99999
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

for chick in combinations(chicken, M):
    total_distance = 0
    for h in home:
        distance = 99999
        for m in range(M):
            distance = min(distance, abs(h[0] - chick[m][0]) + abs(h[1] - chick[m][1]))
        total_distance += distance
    result = min(total_distance,result)


print(result)
def dfs(step, row, col, number):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    number += mapp[row][col]
    
    if step == 6:
        result.append(number)
        return
    
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < 4 and 0 <= new_col < 4:
            dfs(step + 1, new_row, new_col, number)

T = int(input())  
for t in range(T):
    mapp = [input().split() for _ in range(4)]
    
    result = []  
    
    for x in range(4):
        for y in range(4):
            dfs(0, x, y, "")
    
    answer = len(set(result))  
    print(f'#{t+1} {answer}')

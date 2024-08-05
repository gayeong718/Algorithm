def mat_mult(A, B, N):
    # 두 행렬을 곱하는 함수 
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C

def mat_pow(matrix, power, N):
    #행렬의 거듭제곱을 계산하는 함수 
    if power == 1:
        return [[element % 1000 for element in row] for row in matrix]
    elif power % 2 == 0:
        half_pow = mat_pow(matrix, power // 2, N)
        return mat_mult(half_pow, half_pow, N)
    else:
        return mat_mult(matrix, mat_pow(matrix, power - 1, N), N)

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

result = mat_pow(matrix, B, N)

for row in result:
    print(' '.join(map(str, row)))
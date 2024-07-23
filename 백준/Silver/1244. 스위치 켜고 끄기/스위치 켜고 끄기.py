N=int(input())
switch = list(map(int,input().split()))
stu_N=int(input())

# 스위치 함수
def switch_change(switch_num):
    if switch[switch_num] == 1:
        switch[switch_num] =0
    else:
        switch[switch_num] =1


# 남학생
# 받은 수의 배수에 위치하는 스위치 change
def male(M_num):
    for i in range(M_num - 1, N, M_num):
        switch_change(i)

# 여학생
# 받은 수 양 옆의 스위치 상태가 같으면 change.
def female(F_num):
    switch_change(F_num-1)
    for i in range(N):
        if F_num-1-i < 0 or F_num-1+i >= N:
            break
        if switch[F_num-1-i] == switch[F_num-1+i]:
            switch_change(F_num-1-i)
            switch_change(F_num-1+i)
        else:
            break
    return switch

for i in range(stu_N):
    stu_sex, stu_num = map(int,input().split())
    if stu_sex == 1:
        male(stu_num)
    elif stu_sex == 2:
        female(stu_num)




for i in range(0, N, 20):
    print(' '.join(map(str, switch[i:i + 20])))
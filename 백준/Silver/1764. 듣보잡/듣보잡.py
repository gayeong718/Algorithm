
N, M = map(int, input().split())
list_nm=[]
for i in range(N+M):
    list_nm.append(input())



never_heard = list_nm[:N]  
never_seen = list_nm[N:]  

# 교집합
result = sorted(set(never_heard) & set(never_seen))


print(len(result))
for name in result:
    print(name)
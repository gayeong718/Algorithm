def make_tree(idx):
    # idx번째 노드를 루트로하는 트리에 값을 중위순회로 읽은 값
 
    if idx > N:
        return ""
    return make_tree(idx*2) + tree[idx] + make_tree(idx*2+1)
 
 
for t in range(10):
    N = int(input())
    tree = [0] * (N+1)
    for _ in range(N):
        node, ch, *child = input().split()
        tree[int(node)] = ch
 
    print(f'#{t+1} {make_tree(1)}')
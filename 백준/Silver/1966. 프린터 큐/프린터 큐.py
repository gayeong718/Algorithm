from collections import deque

T = int(input())  
for _ in range(T):
    N, M = map(int, input().split())  
    queue = deque(map(int, input().split()))  
    queue = deque([(priority, idx) for idx, priority in enumerate(queue)])  # (우선 순위, 인덱스) 

    count = 0  # 출력된 문서의 개수
    while True:
        # 현재 맨 앞 문서가 가장 높은 우선 순위를 가지는지 확인
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1  # 출력된 문서 개수 증가
            if queue[0][1] == M:  # 궁금한 문서의 인덱스인 경우
                print(count)  # 출력된 문서의 개수 출력
                break  
            else:
                queue.popleft()  # 맨 앞 문서 제거
        else:
            queue.append(queue.popleft())  # 맨 앞 문서를 큐의 맨 뒤로 이동
T = int(input())

for t in range(1,T+1):
    num_list = list(input().split())

    # 현재 위치
    B = 1
    O = 1
    bt = 0
    ot = 0
    N = int(num_list.pop(0))
    prev = num_list[0]

    for i in range(0, N*2, 2):
        robot = num_list[i]
        btn = int(num_list[i+1])


        #이전 로봇과 같을 때
        if prev == robot:
            if robot == "B":
                bt = bt + abs(btn-B) + 1 
                B = btn
            else:
                ot = ot + abs(btn-O) + 1
                O = btn

        else:
            if robot == "B":
                if bt + abs(btn-B) + 1 <= ot:
                    bt = ot + 1
                else:
                    bt = bt + abs(btn-B) + 1
                B=btn
            else:
                if ot + abs(btn-O) + 1 <= bt:
                    ot = bt + 1
                else:
                    ot = ot + abs(btn-O) + 1
                O=btn
        prev = robot


    print(f'#{t} {max(bt,ot)}')
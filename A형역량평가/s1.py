"""
강가를 따라서 낚시터 자리가 1~N까지 일렬로 늘어서 있다. 낚시터에는 3개의 출입구가 있으며,
각 출입구에는 낚시터에 입장하기 위해 대기하고 있는 낚시꾼들이 각각 존재한다.

모든 낚시꾼들은 한 사람당 하나의 낚시터에 자리를 잡아야 하며, 자리를 잡는 절차는 다음과 같다.

1. 혼잡을 피하기 위해 하나의 출입구씩 선택하여 순차적으로 입장 할 수 있다.

2. 출입구가 선택되면, 해당 출입구에 대기하고 있는 낚시꾼들은 자신의 위치에서 가장 가까운 빈 낚시터 자리로 한 명씩 이동하여 차례대로 자리를 잡는다.
  - 출입구에서 바로 위쪽의 낚시터까지의 거리는 1m 이며, 좌우로 한 칸씩 멀어질 때 마다 추가로 1m씩 멀어진다.
  - 예를 들어 [Fig. 1]의 Gate1에서 4번 자리까지는 1m 이고, 3번과 5번자리는 2m의 거리가 된다.

3. 해당 출입구의 맨 마지막 사람의 경우, 가장 가까운 빈 자리가 두 곳이라면 하나를 선택해야 한다.
   (맨 마지막 사람이 아닌 경우, 두 곳 중 아무데나 가도 결과는 같으므로 고려할 필요가 없다.)

4. 해당 출입구에 대기중인 모든 낚시꾼들의 자리잡기가 완료되면, 다음 출입구를 선택하여 위 1~3 과정을 반복 수행한다.


낚시터 자리의 개수 N이 주어지고, 출입구 3개의 위치 및 해당 출입구에 대기중인 각각의 낚시꾼들의 숫자가 주어진다.
이때 위의 낚시터 자리잡기 절차를 수행하면서 낚시꾼들 각각의 이동거리를 모두 더한 값이 최소가 되도록 자리잡는 방법을 찾고, 그때의 이동거리의 합을 출력하라.


예를 들어 앞의 [Fig. 1]과 같이, 낚시터 정보가 다음과 같이 주어졌을 경우를 살펴보자.
 - 낚시터 자리 개수 N=10
 - 1번 출입구의 위치=4, 낚시꾼들의 숫자=5명
 - 2번 출입구의 위치=6, 낚시꾼들의 숫자=2명
 - 3번 출입구의 위치=10, 낚시꾼들의 숫자=2명

----------------------------------------------------------------------------------
[제약사항]
1. 낚시터의 개수 N은 5 이상 60 이하의 정수 (5 ≤ N ≤ 60)
2. 출입구는 항상 3개이다.
3. 각 출입구에 대기하고 있는 낚시꾼들의 수는 1 이상 20 이하의 정수
4. 낚시터의 자리가 부족하여 낚시꾼들이 자리를 잡지 못하는 경우는 입력으로 주어지지 않는다.
5. 두 개의 출입구에서 동시에 낚시꾼들이 입장하는 것은 불가능 하며, 반드시 하나의 출입구에 있는 모든 낚시꾼들의 배치가 끝나야 다른 출입구의 입장이 가능하다. 


[입력]
입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T가 주어지고, 그 다음 줄부터 T개의 테스트 케이스가 주어진다.
테스트 케이스의 첫 번째 줄에는 낚시터 자리의 개수 N이 주어진다.
그 다음 줄부터 3줄에 걸쳐 각각 두 개의 숫자가 주어진다. 첫 번째 숫자는 출입구의 위치이며, 두 번째 숫자는 해당 출입구에 대기하고 있는 낚시꾼들의 수 이다.


[출력]
출력은 "#t"를 찍고 한 칸 띄운 다음 정답을 출력한다. (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
정답은 각 낚시꾼들의 이동거리의 합이 최소가 될 때의 그 값이다.
"""

T = int(input())

for t in range(1, T+1):
    # 출입구의 위치와 그 위치에서 기다리는 낚시꾼
    N = int(input())
    position = []
    waiting_person = []
    for i in range(3):
        p, w = map(int, input().split())
        position.append(p)
        waiting_person.append(w)

    # 순서별로 최소 거리 계산
    move_cnt = 987654321
    for cnt in range(3):
        # N의 개수만큼의 낚시터의 자리 생성
        fish_sit = [0]*N
        tmp_cnt = 0
        # 오른쪽으로 한 자리씩 넘기면서 tmp_cnt 확인
        for m in range(3):
            # 임시 저장이 더 커지면 계산할 필요가 없으므로 break
            if tmp_cnt > move_cnt:
                break

            if m:
                pass
            # 첫번째 게이트 오픈
            else:
                fir_gate_wait_person = waiting_person[cnt]
                if fir_gate_wait_person %2:
                    for f in range(fir_gate_wait_person):
                        ran = (fir_gate_wait_person + 1)//2
                        if min(position[cnt], N-position[cnt]) < ran:
                            #문제발생
                            pass
                        else:
                            for r in range(fir_gate_wait_person):
                                fish_sit[position[cnt]-ran+r] = 1
                                tmp_cnt += ran*(ran+1) -1
    print('#{} {}'.format(t, move_cnt))
                                
        

"""
sample Input
5
10
4 5
6 2
10 2
10
8 5
9 1
10 2
24
15 3
20 4
23 7
39
17 8
30 5
31 9
60
57 12
31 19
38 16

sample Output
#1 18
#2 25
#3 57
#4 86
#5 339
"""
    

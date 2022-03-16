T = int(input())

for tc in range(1, T+1):
    N = int(input())
    place = [0 for _ in range(N)]
    
    gate = []
    fisher = []
    for i in range(3):
        a, b = map(int, input().split())
        gate.append(a)
        fisher.append(b)
    
    
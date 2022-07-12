def solution(n):
    if n%2:
        return 0
    cases = [0, 3]
    n /= 2
    while len(cases)<n+1:
        case = 0
        for c in range(len(cases)):
            case += 2*cases[c]
        case += cases[-1] + 2
        cases.append(case%1000000007)
    return cases[-1]

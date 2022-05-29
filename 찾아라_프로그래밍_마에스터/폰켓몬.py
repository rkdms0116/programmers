def solution(nums):
    # 선택할 폰켓몬 개수
    N = len(nums)//2
    # 폰켓몬의 종류 개수
    kind = len(set(nums))
    # 선택할 수 있는 폰켓몬의 개수와 종류의 개수 중 더 작은 개수가 정답
    answer = min(N, kind)
    return answer

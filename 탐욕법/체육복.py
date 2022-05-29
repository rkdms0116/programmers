def solution(n, lost, reserve):
    # 여분의 옷이 있는 학생과 체육복을 도난당한 학생을 students list에 확인
    students = [0]*(n+1)
    for lo in lost:
        students[lo] -= 1
    for re in reserve:
        students[re] += 1

    i = 0
    while i < len(students):
        # 분실당한 학생이라면,
        if students[i] == -1:
            # 1. 왼쪽에 있는 학생이 여분의 체육복을 가지고 있다면,
            if i-1 > -1 and students[i-1] > 0:
                students[i-1] -=1
                students[i] += 1
            # 2. 왼쪽 학생이 체육복이 없다면, 오른쪽 학생의 체육복 확인
            elif i+1 < len(students) and students[i+1] > 0:
                students[i+1] -= 1
                students[i] += 1
        i += 1
    # 정답 : 전체 n명에서 -1의 개수를 제외
    answer = n - students.count(-1)
    return answer
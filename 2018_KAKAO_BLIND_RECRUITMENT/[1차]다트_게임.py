def solution(dartResult):
    answer = 0
    score = []
    idx = 0
    while idx < len(dartResult):
        if dartResult[idx].isnumeric():
            # 점수가 0 ~ 10점이므로 10점일 경우
            if int(dartResult[idx]) == 1:
                if dartResult[idx+1].isnumeric():
                    dart = 10
                    idx += 1
                else:
                    dart = int(dartResult[idx])
            else:
                dart = int(dartResult[idx])
            
            # Bonus 확인 후 score에 append
            if dartResult[idx+1] == "S":
                score.append(dart)
            elif dartResult[idx+1] == "D":
                score.append(dart**2)
            elif dartResult[idx+1] == "T":
                score.append(dart**3)
            # index 증가    
            idx += 2

        # option 확인
        if idx < len(dartResult) and dartResult[idx] in ["*", "#"]:
            option_num = len(score)
            if dartResult[idx] == "*":
                # "*"이 나왔을 경우 앞 점수까지 double이므로 score의 len확인
                if option_num ==1:
                    score[0] = score[0] * 2
                else:
                    score[option_num-2] = score[option_num-2] * 2
                    score[option_num-1] = score[option_num-1] *2

            elif dartResult[idx] == "#":
                score[option_num-1] = score[option_num-1] * (-1)
            idx += 1

    # score의 합계를 answer에 더함
    for s in score:
        answer += s
                
    return answer


# 점수가 당연히 0~9점이라 생각하고 문제를 풀어서 조금 꼬였다.
# index가 헷갈려서 index-error가 좀 있었다.
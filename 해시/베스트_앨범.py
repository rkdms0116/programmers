def solution(genres, plays):
    answer = []
    # play_gen = {장르 : 장르 누적 재생 횟수}
    play_gen = {}
    for gen in range(len(genres)):
        if genres[gen] in play_gen:
            play_gen[genres[gen]] += plays[gen]
        else:
            play_gen[genres[gen]] = plays[gen]
    # genresNplays : play_gen 내림차순 정렬
    genresNplays = sorted(play_gen.items(), key = lambda item: item[1], reverse=True)

    # playNindex : {index : [장르, 곡 재생 횟수]}
    playNindex = {}
    for num in range(len(plays)):
        if genres[num] not in playNindex:
            playNindex[num] = [genres[num], plays[num]]
        else:
            playNindex[num] = [genres[num], plays[num]]

    # 최대 장르를 for문으로 순회하면서
    for n in range(len(genresNplays)):
        play_list = {}
        # playNindex의 장르가 만약에 일치한다면
        for i in range(len(playNindex)):  
            if genresNplays[n][0] == playNindex[i][0]:
                # play_list = {index : 재생 횟수}
                play_list[i] = playNindex[i][1]
        # play 수에 따라 정렬
        temp_list = sorted(play_list.items(), key = lambda item: item[1], reverse=True)
        # 첫번째 인덱스 저장
        answer.append(temp_list[0][0])
        # temp_list가 2개 이상이라면 1개만 더 저장하고 종료
        if len(temp_list) > 1 :
            answer.append(temp_list[1][0])
    return answer

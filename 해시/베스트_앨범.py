def solution(genres, plays):
    answer = []
    """
    # 장르/장르의 재생 횟수
    play_gen = {}
    # 장르/노래 index/재생 횟수
    play_song = {}
    for gen in range(len(genres)):
        if gen in play_gen:
            play_gen[genres[gen]] += plays[gen]
        else:
            play_gen[genres[gen]] = plays[gen]
    # 가장 많이 재생된 장르대로 순서
    sort_play = sorted(play_gen.items(), key = lambda item: item[1], reverse=True)
    print(sort_play)
    """
    # genres와 plays dictionary 형태로 묶어서 최대 play된 장르 순서대로 정렬
    genresNplays = sorted(dict(zip(genres, plays)).items(), key = lambda item: item[1], reverse=True)
    """
    play = {}
    while plays:
        for n in range(len(genres)):
            play_genre = {}
            for g in range(len(genresNplays)):
                if genres[n] == genresNplays[g]:
                    play_genre[n] = plays[n]
                    plays.pop(plays[n])
            play_genre_sort = sorted(play_genre.items(), key = lambda item: item[1], reverse=True)
            for sor in range(len(play_genre_sort)):
                answer.append(play_genre_sort)
    print(play)
    """
    playNindex = {}
    for num in range(len(plays)):
        if genres[num] not in playNindex:
            playNindex[num] = [genres[num], plays[num]]
        else:
            playNindex[num] = [genres[num], plays[num]]
    print(playNindex)
    for gen in genresNplays:
        for idx in range(len(playNindex)):
            if playNindex[idx][1] == gen:
                pass
    return answer
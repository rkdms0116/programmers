def solution(user_ids, banned_ids):
    possibility = set()
    for banned_id in banned_ids:
        for user_id in user_ids:
            # banned id와 user id의 길이가 일치한다면, * 외의 문자가 일치하는지 test
            if len(banned_id) == len(user_id):
                for l in range(len(banned_id)):
                    if banned_id[l] == "*":
                        pass
                    else:
                        if banned_id[l] != user_id[l]:
                            break
                else:
                    possibility.add(user_id)
    # print(possibility)
    answer = len(possibility) - len(banned_ids) + 1
    return answer


print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]))
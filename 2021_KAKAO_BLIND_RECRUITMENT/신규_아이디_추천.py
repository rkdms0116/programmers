def solution(new_id):
    fir = new_id.lower()
    poss = ['-', '_', '.']
    sec = ''
    for f in fir:
        if f.isdigit() or f.isalpha() or f in poss:
            sec += f
    thr = sec     
    while True:
        if '..' in thr:
            thr = thr.replace('..', '.')
        else:
            break
    
    fou = thr
    if fou and fou[0] == '.':
        fou = thr[1:]
    if fou and fou[-1] == '.':
        fou = fou[:-1]
    
    fiv = fou
    if not fiv:
        fiv = 'a'
    
    six = fiv
    if len(fiv) > 15:
        six = fiv[:15]
    if six[-1] == '.':
        six = six[:-1]
    
    if len(six) == 1:
        answer = six * 3
    elif len(six) == 2:
        answer = six + six[-1]
    else:
        answer = six
    
    return answer
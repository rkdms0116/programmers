# 입출차 시간을 담은 list
def timeToMin(parkingTime):
    temp = []
    time = 0
    # str 형식의 시간을 min 타임으로 변환
    for parking in parkingTime:
        hh, mm = map(int, parking.split(':'))
        temp.append(hh*60 + mm)
    # 출차된 기록이 없을 경우(출차내역이 없을 시 23:59 (1439)에 출차한 것으로 간주)
    if len(temp) % 2:
        for t in range(len(temp), -1, -2):
            if t == len(temp):
                time += 1439-temp[t-1]
            else:
                time += temp[t] - temp[t-1]
    # 입,출차의 기록이 모두 있을 경우
    else:
        for t in range(len(temp)-1, 0, -2):
            time += temp[t] - temp[t-1]
    return time

def solution(fees, records):
    answer = []
    receipts = dict()
    # carNumber와 입출차 time을 담은 dictionary
    for record in records:
        time, carNum, state = record.split()
        if carNum in receipts:
            receipts[carNum].append(time)
        else:
            receipts[carNum] = [time]
    # carNumber로 정렬
    receipts = sorted(receipts.items(), key = lambda item: item[0])
    
    for receipt in receipts:
        m = timeToMin(receipt[1])
        # 주차요금 계산 시작
        pay = 0
        # 기본 주차 시간보다 오래 있었을 경우
        if m > fees[0]:
            pay += fees[1]
            if (m-fees[0])%fees[2]:
                pay += ((m-fees[0])//fees[2] + 1)*fees[3]
            else:
                pay +=  ((m-fees[0])//fees[2])*fees[3]
            answer.append(pay)
        # 기본 주차 시간 내에서 있었을 경우
        else:
            answer.append(fees[1])   
    return answer

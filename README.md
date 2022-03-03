# 💻 programmers

```
Algorithm 문제를 매일매일 풀어봅시다!
```



### 🗓 3/1

✅ 완주하지 못한 선수
✅ 위장

````
hash에 대해서 배웠다!
python의 경우 dictionary로 구현한다.
SSAFY 처음에만 해도 dictionary를 전혀 사용하지 못했는데 쉬운 문제부터 풀어보니 자신감이 조금 붙었다!
조금 더 코드를 깔끔하게 짜보고싶다 :)
````

### 🗓 3/2

⬜ 베스트앨범
✅ 프린터

```
프린터의 경우, 다른 팀원분이 원형 큐를 이용하여 문제를 푸셨는데 다음에 원형큐로 풀어봐야겠다! :)
```

### 🗓 3/3

✅ 다리를 지나는 트럭
✅ 주식가격

```
다리를 지나는 트럭의 경우 팀원분들과 이야기를 해본 결과
	sum 함수를 계속 이용하면 시간이 오래걸릴 것!
	deque를 활용해서 해보자!

주식가격의 경우 deque를 활용해서 문제를 풀었다!
근본적으로 왜 속도차이가 나는지를 잘 모르겠다ㅜㅠ
```

```python
    while stocks:
        # 가장 왼쪽 주식 값 추출
        stock = stocks.popleft()
        time = 0
        # 남아있는 주식들의 가격을 확인하면서
        for price in stocks:
            time += 1
            # 왼쪽 값이 더 큰 순간 멈춤
            if stock > price:
                break
        # for문이 정상적으로 끝나거나 break 걸려도 값 추가
        answer.append(time)
```

💡 마지막에 if문 안에 append를 해줬었는데 생각해보니까 break가 걸려도 for문이 끝나기 때문에 append가 되어서 두 번 들어가는 상황이 발생했었다! 주의하자!

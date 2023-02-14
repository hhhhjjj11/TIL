# 알아두기1 : 큐가 왼쪽으로 돈다 = 앞에꺼 빼서 뒤에 append
#            오른쪽으로 돈다 = 뒤에꺼 빼서 앞으로
# 알아두기2 : 뒤로도는게 가깝냐 앞으로도는게 가깝냐 판별방법
#              방법1. (idx1-idx2)%(len(li)) 랑 (idx2-idx1) % len(li) 비교
#                       근데 이경우 idx1이랑 idx2랑 뭐가더 앞에 있냐에 따라 케이스 나눠야함주의
#              방법2. 스택이나 큐를 쓸경우 항상 하나는 첫번째 항이므로, 다음처럼 판별 가능.
#                       idx2가 len(li)/2보다 크면 뒤로도는게 더 빠르고 
#                                           작으면 앞으로 도는게 더 빠름. 

from collections import deque

N, M = map(int,input().split())

li = list(map(int,input().split()))

deck = deque(i for i in range(1,N+1))

cnt = 0

for idx in list:
    while True:
        if deck[0] == idx:
            deck.popleft()
            break
        else:
            if deck.index(idx) < len(deck)/2:
                while deck[0] != idx:
                    deck.append(deck.popleft())
                    cnt+=1
            else:
                while deck[0] != idx:
                    deck.appendleft(deck.pop())
                    cnt+=1
print(cnt) 
N = int(input())
cnt=0

for i in range(1, N//3+1):    
    M = int(max([i,N//2+1-i]))
    cnt+=len(range(M,(N-i)//2+1))   

print(cnt)


# 알고가기
# 1. 메모리와 시간 사용을 줄이기 위해, 빠르게 작동할 수 있도록
#    컴퓨터가 할 일을 줄여줘야함.!!

# 무슨얘기냐. 다음의 두가지 방법을 비교.

# 방법 1. 모든 3가지 순서쌍을 구해놓고, 필터를 통해 작은 두변의 합이 
# 가장큰 변 보다 큰 경우만을 남기고나서, 겹치는 것들을 하나로 세고, 최종적으로
# 남은 것들의 개수를 출력.

# 방법 2. 가장 작은 변의 길이는 1~N//3+1만이 가능하므로, 해당범위만 반복하도록 하고,
# 두번째로 작은 변의 길이는 [가장작은변, N//2+1에서 가장작은 변을 뺀 것]중에 큰 최대값
# 부터 가능하므로, 또 그 범위만 반복하도록하고, 그렇게 첫번째 변과 두번째 변을 정하면
# 세번째 변은 자동으로 유일하게 정해지므로, 세번째 변은 따로 처리하지 않고 그냥
# cnt를 세주면 된다. 


# 방법1의 예시
# 다음과 같이 작성하면 메모리초과 난다. 시간초과도 난다.

# for i in range(1, int(N/2)+1):  # 1~49
#     for j in range(1, N-i): # i =3 
#         li = [i,j,N-i-j]
#         li.sort()
        
#         li=tuple(li)
#         if li[0]+li[1]>li[2]:
#             res.append(li)
    
# for item in res:
#     item=list(item)
#     item.sort()
#     item=tuple(item)

# #print(res)
# print(len(Counter(res).keys()))
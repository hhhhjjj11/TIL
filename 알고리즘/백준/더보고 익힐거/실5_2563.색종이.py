N = int(input())
papers=[]
for _ in range(N):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            papers.append((x+i,y+j))
   
papers = set(papers)
papers = list(papers)

print(len(papers))

# 아이디어 기억하기 
# 한칸씩, 전부다 배열에 추가하고 집합으로 바꾸기 ->중복된거 다날라감 개꿀
A,B=map(int,input().split())  # 3,7
li=[]
res=0
n=1
while len(li) <= B:
    for _ in range(n):
        li.append(n)
    n+=1

print(li)


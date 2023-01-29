li = list(map(int,input().split()))

n=0
cnt=0
while True:
    if cnt==3:
        break
    n+=1
    cnt=0
    for item in li:
        if n % item==0:
            cnt+=1
            if cnt==3:
                break

print(n)

# while문 쓸 때 주의사항
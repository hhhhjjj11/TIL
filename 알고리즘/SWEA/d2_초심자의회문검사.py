T = int(input())
for t in range(1,T+1):
    res=0
    str=input()

    if str==str[::-1]:
        res=1

    print(f'#{t} {res}')
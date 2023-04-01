A1, B1 = map(int,input().split())
A2, B2 = map(int,input().split())

bunja = A1*B2 + A2*B1
bunmo = B1*B2

#print(bunja,bunmo)

# 분자와 분모를 각각 소인수 분해한다.
# 각각 겹치는거 빼준다.
# 그럼끝.

def soinsoo(N):
    result =[]

    chae = [False]*(N+1)
   
    for div in range(2,N+1):
        if not chae[div] and N%div == 0:
            while N%div == 0:
                result.append(div)
                N //= div
            #print('div',div)
            m = 2
            while div*m<N:
                chae[div*m] = True
                m += 1
      

    return result

a1 = soinsoo(bunja)
a2 = soinsoo(bunmo)
#print('!',a1,a2)

# 만약에 분자 소인수분해한것안에 분모 항이랑 겹치면
check_a2 = [0]*len(a2)
temp1 =[]
for i in range(len(a1)):
    brk = False
    for j in range(len(a2)):
        if a1[i] == a2[j] and check_a2[j] == 0:
            check_a2[j] = 1
            #print('index',i,j)
            #print('check',check_a2)
            brk =True
            break
    if brk:
        continue
    temp1.append(a1[i])

#print('분자최종',temp1)
bonja = 1

for x in temp1:
    bonja *= x

# 이제 분모는 체크안된애들만 곱해주면 됨
bonmo = 1

for i in range(len(check_a2)):
    if not check_a2[i]:
        #print('a2[i]', a2[i])
        bonmo *= a2[i]

print(bonja,bonmo)
T = int(input())

for tc in range(1,T+1):
    N = int(input())
    cnts =['X']*51
    li = list(map(int,input().split()))

    for item in li:
        if cnts[item] == 'X':
            cnts[item] =1
        else:
            cnts[item] +=1
    
    print(f'#{tc}',end=' ')
    
    for index, value in enumerate(cnts):
        if value != 'X':
            while value > 0:
                print(index,end=' ')
                value-=1

    print('')



# Sol2. Bubble정렬 이용

# T = int(input())

# for tc in range(1,T+1):
#     N = int(input())
#     li = list(map(int,input().split()))

#     for i in range(len(li)-1,0,-1): 
#         for j in range(i):
#             if li[j] > li[j+1]:
#                 li[j],li[j+1] = li[j+1],li[j]

#     print(f'#{tc}',end=' ')
#     for i in range(len(li)):
#         print(li[i], end=' ')
#     print('')



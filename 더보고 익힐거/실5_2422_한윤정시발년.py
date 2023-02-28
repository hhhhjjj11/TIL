# 시도2. 집합연산이용(드모르간, 집합의 덧셈정리 이용) 두개 교집합까지는 굿인데 
# 세개교집합 갯수 구하는 부분에서 시간초과..

N, M = map(int,input().split())
d={}

for i in range(M):
    p,q = map(int,input().split())
    d[p]=d.get(p,{q})
    d[p].add(q)
    d[q]=d.get(q,{p})
    d[q].add(p)

#print(d)
cnt = 0
keys = list(d.keys())
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if i in keys and j in d[i]:
            continue
        else:
            for k in range(j+1,N+1):
                if j in keys and k in d[j]:
                    continue
                if k in keys and i in d[k]:
                    continue
                #print({i,j,k})
                cnt+=1

print(cnt)



# 시도2. 집합연산이용(드모르간, 집합의 덧셈정리 이용) 두개 교집합까지는 굿인데 
# 세개교집합 갯수 구하는 부분에서 시간초과..

# def C(n,r):
#     res=1
#     for i in range(r):
#         res*=n
#         n-=1
#     for i in range(2,r+1):
#         res/=i
#     return res

# N, M = map(int,input().split())
# d={}
# NO=[]
# for i in range(M):
#     p,q = map(int,input().split())
#     NO.append({p,q})
#     d[p]=d.get(p,{q})
#     d[p].add(q)
#     d[q]=d.get(q,{p})
#     d[q].add(p)

# #print(d)
# ans = C(N,3)-M*(N-2)
# cnt = 0
# for s in d.values():
#     if len(s)>1:
#         cnt += C(len(s),2)

# ans += cnt

# 교집합세개
# cnt2=0
# for i in range(len(NO)):
#     for j in range(i+1,len(NO)):
#         if len(NO[i] | NO[j]) == 4:
#             continue
#         elif len(NO[i] | NO[j]) == 3:
#             for k in range(j+1,len(NO)):
#                 if len(NO[i] | NO[j] | NO[k])==3:
#                     cnt2+=1

# ans -= cnt2

# print(int(ans))






# 시도1. 경우 다 구해서 일일이 푸는 법 // 정답이지만 시간초과 메모리초과

# N ,M = map(int,input().split())


# res = []

# for i in range(1, N+1):
#     for j in range(i+1, N+1):
#         for k in range(j+1, N+1):
#             res.append({i,j,k})    #여기서 이미 메모리 초과 뜸.

# print(len(res))
# print(res)

# NO = {}
# #print('NO', NO)
# for _ in range(M):
#     p,q = map(int,input().split())
    
#     NO[p] = NO.get(p,{q})
#     NO[p].add(q)

# #print(NO)


# cnt=0
# 탈락cnt =0
# for i in range(len(res)):  # 결과들 모아놓은것
#     isRight=True
#     for key,value in NO.items():  # 금지조합의 인덱스와 각항
#         for num in value:
#             if len(res[i] - {key,num}) == 1 :
#                 print(res[i],'탈락')
#                 탈락cnt+=1
#                 isRight=False
#                 break
#         if isRight==False:
#             break
#     if isRight==False:
#         continue
#     cnt+=1
        
# print(cnt)
# print('탈락',탈락cnt)

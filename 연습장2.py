# 1~5 가지고 순열 만들기

res = []


for i in range(1,6):
    stack = []
    visited=[False]*6
    stack.append(i)
    visited[i] = True
    
    temp=[]
    
    while stack:
        
        X = stack.pop()

        for j in range(1,6):
            if not visited[j]:
                temp.append(j)
                visited[j] = True
                
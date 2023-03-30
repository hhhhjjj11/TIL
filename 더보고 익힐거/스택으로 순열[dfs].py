li = [1,2,3,4]

# dfs 로 스택 순열 구현하기

stack = [[x] for x in li] # 뭐가들어가야할가..

results = []

while stack:
    
    permu = stack.pop()
    #print(permu)
    if len(permu) == len(li):
        results.append(permu)
    for candidate in li:
        if candidate not in permu:
            stack.append(permu + [candidate])

print('results',results)
print('len',len(results))
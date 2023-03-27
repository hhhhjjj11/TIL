li = [1,2,3,4]

stack = [[[],[0,0,1,1]]]
results = []

print('stack',stack)
while stack: 
    permutation, used = stack.pop(0)
    print(permutation, used)
    if len(permutation) == len(li):
        results.append(permutation)
        continue  
    for i in range(len(li)): 
        if not used[i]:
            used[i] = 1 
            #print('used',used)
            stack.append([permutation+[li[i]], used])
            #print('used after',used)
            used[i] = 0

print(results)


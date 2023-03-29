li = [1,2,3,4]

stack=[[[x],[i]] for i,x in enumerate(li)]

permutations = []

while stack:
    permutation, indexes = stack.pop()

    if len(permutation) == len(li):
        permutations.append(permutation)

    else:
        for k in range(len(li)):
            if not k in indexes:
                stack.append([permutation + [li[k]], indexes + [k]])

permutations.sort()
print('perms')
print(permutations)

stack2 = [[[x],i] for i,x in enumerate(li)]
n = 2
combs =[]
while stack2:
    comb, last_idx = stack2.pop()
    if len(comb) == n:
        combs.append(comb)
    else:
        for j in range(last_idx + 1, len(li)):
            stack2.append([comb+[li[j]], j])

print('combs')
print(combs)
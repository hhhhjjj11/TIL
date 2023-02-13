li = [ 1,2,3,4,5,6]


subsets = []
for i in range(1<<len(li)):
    s = set()
    for n in range(len(li)):
        if i & 1<<n:
            s.add(li[n])
    subsets.append(s)
    
subsets.append(set())
print(subsets)

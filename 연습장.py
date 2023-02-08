M = int(input())


for _ in range(M):
    inp = input()
    if inp == 'empty' or inp=='all':
        c=inp
    else :
        c,n = inp.split()
    s=set()
    if c == 'add':
        s.add(n)
        print(s)
    if c == 'check':
        print('n',n)
        if str(n) in s:
            print(1)
        else:
            print(0)
    if c == 'remove':
        s.discard(n)
    if c == 'toggle':
        if n in s:
            s.remove(n)
        else:
            s.add(n)
    if c == 'all':
        s ={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    if c == 'empty':
        s = set()
    
    
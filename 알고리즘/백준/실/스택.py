from sys import stdin

N = int(input())

stack = []

for _ in range(N):
    A = stdin.readline().rstrip()
    B = A.split()
    if len(B)>1:
        A,n =B
    if A == 'push':
        stack.insert(0,n)
    elif A == 'top':
        try:
            print(stack[0])
        except:
            print(-1)
    elif A == 'size':
        print(len(stack))
    elif A == 'empty':
        if len(stack) == 0 :
            print(1)
        else:
            print(0)
    elif A == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            x = stack[0]
            stack.pop(0)
            print(x)


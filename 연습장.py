n = int(input())

li = [0, 1, 3]

for _ in range(998):
    li.append(0)

def sol(n):
    if li[n] != 0:
        return li[n]
    else:
        li[n] = 2*sol(n-2)+sol(n-1)
        return li[n]

print(sol(n)%10007)
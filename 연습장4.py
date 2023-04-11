A, B, C = map(int,input().split())

rest = 1

while B > 0:
    if B % 2 == 1:
        B -= 1
        rest *= A
        rest %= C
    elif B % 2 == 0:
        B //= 2
        rest = rest ** 2
        rest %= C

print(rest)
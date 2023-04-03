def findrep(i): # 대표원소를 찾아주는 함수
    while rep[i] != i:
        i = rep[i]
    return i

def union(x, y):
    rep[findset(y)] = findeset(x)

rep = list(range(7))

union(1,3)
union(2,3)
union(5,6)
print(findset(6))
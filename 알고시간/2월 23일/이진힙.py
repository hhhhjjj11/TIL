T = int(input())

def enq(n):
    global last
    last +=1
    heap[last] = n
    c = last
    p = c//2
    while p>0 and heap[p]>heap[c]:
        heap[p],heap[c] = heap[c],heap[p]
        c = p
        p = c//2

for tc in range(1,T+1):
    res = 0
    N = int(input())
    li = list(map(int,input().split()))

    heap = [0]*(N+1)
    last = 0

    for i in li:
        enq(i)

    res = 0
    node_num = N//2
    while node_num>0:
        res += heap[node_num]
        node_num//=2
    print(f'#{tc} {res}')
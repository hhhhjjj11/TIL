for tc in range(1,11):
    res = 0
    N = int(input())

    heap=[0]*(N+1)
    c1 = [0]*(N+1)
    c2 = [0]*(N+1)
    for _ in range(N):
        li = list(input().split())
        if len(li) ==4:
            node_num , op, child1,child2= li
            node_num = int(node_num)
            child1 = int(child1)
            child2 = int(child2)
            heap[node_num] = op
            c1[node_num] = child1
            c2[node_num] = child2

        elif len(li) ==  2:
            node_num , child = list(map(int,li))
            heap[node_num] = child

    for i in range(N,0,-1):
        if heap[i] in ('-','*','/','+'):
            if heap[i] =='-':
                heap[i]=heap[c1[i]]-heap[c2[i]]
            if heap[i] =='+':
                heap[i]=heap[c1[i]]+heap[c2[i]]
            if heap[i] =='*':
                heap[i]=heap[c1[i]]*heap[c2[i]]
            if heap[i] =='/':
                heap[i]=heap[c1[i]]/heap[c2[i]]

    print(f'#{tc} {int(heap[1])}')
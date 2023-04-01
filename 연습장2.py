
li = [1, 2, 3, 24, 666, 4, 434, 3, 355, 544, 3333, 566, 4]

def merge_sort(s,e):
    if s == e:
        return
    
    mid = (s+e)//2

    merge_sort(s,mid)
    merge_sort(mid+1, e)
    
    cur1 = s
    cur2 = mid+1

    temp = []

    while cur1<=mid and cur2<=e:
        if li[cur1] <= li[cur2]:
            temp.append(li[cur1])
            cur1+=1
        else:
            temp.append(li[cur2])
            cur2+=1
    
    while cur1<=mid:
        temp.append(li[cur1])
        cur1 += 1

    while cur2<=e:
        temp.append(li[cur2])
        cur2 += 1
    
    for i in range(s,e+1):
        li[i] = temp[i-s]
    

merge_sort(0,len(li)-1)

print(li)
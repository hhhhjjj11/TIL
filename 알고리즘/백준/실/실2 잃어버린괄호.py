li = input()
# li = li.split('-')

if li[0] == '-':
    pass
    arr = li.split('-')
    res = 0
    for i in arr:
        temp = i.split('+')
        for num in temp:
            res -= int(num)
    print(res)
else:
    pass
    arr = li.split('-')
    res = 0
    for i in range(len(arr)):
        if i ==0:
            temp = arr[0].split('+')
            for num in temp:
                res+= int(num)
        else :
            temp = arr[i].split('+')
            for num in temp:
                res -= int(num)
    print(res)
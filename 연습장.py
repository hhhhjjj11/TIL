li = [1,2,3,2,1,1]

for i in li:
    if li.count(i) > 1:
        print(i,li.count(i))
        print('중복')
        break
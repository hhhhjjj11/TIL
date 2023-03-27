li = [0]*3

test = [[[],li]]

while test:
    temp, li = test.pop()
    print(li)
    for i in range(2):
        if i==1:
            li[i] = 10
            test.append([temp,li])
            

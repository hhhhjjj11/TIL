gruop_number = 0
while True:
    gruop_number += 1
    N = int(input())
    if N == 0 : 
        break
    dic={}
    for _ in range(N):
        li = list(input().split())
        dic[li[0]] = dic.get(li[0],li[1:])

    #print(dic)
    result=[]
    for key, value in dic.items():
        for index, message in enumerate(value):
            if message == 'N':
                count = index+1
                result.append(f'{list(dic.keys())[list(dic.keys()).index(key)-count]} was nasty about {key}')
    if gruop_number != 1:
        print('')
    print(f'Group {gruop_number}')
    if len(result) == 0:
        print('Nobody was nasty')
    else:
        for item in result:
            print(item)
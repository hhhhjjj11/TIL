import re

N = int(input())

def merge_sort(low, high):

    # print('low','high',low,high)
    # print('serials',serials)
    if high-low < 2:
        return

    mid = (low + high)//2

    merge_sort(low, mid)
    merge_sort(mid, high)

    temp = []

    l, h = low, mid
    # print('low','mid',l,h)
    while l < mid and h < high:
        if len(serials[l]) < len(serials[h]):
            temp.append(serials[l])
            l += 1
        elif len(serials[l]) > len(serials[h]):
            temp.append(serials[h])
            h += 1
        # 길이가 같으면 다음 조건으로 넘어가야 함 : 숫자합 비교
        elif len(serials[l]) == len(serials[h]):
            numbers1 = re.sub(r'[^0-9]', '', serials[l])
            numbers2 = re.sub(r'[^0-9]', '', serials[h])
            if not numbers1:            # 숫자 없으면 0으로 취급한다. 그래서 앞으로 가게.
                sum1 = 0
            else:
                sum1 = sum(list(map(int,list(numbers1))))
            if not numbers2:
                sum2 = 0
            else:
                sum2 = sum(list(map(int,list(numbers2))))
            # print('numbers1',numbers1)
            # print('numbers2',numbers2)
            if sum1 < sum2:
                temp.append(serials[l])
                l += 1
            elif sum1 > sum2:
                temp.append(serials[h])
                h+=1
            elif sum1 == sum2:
                # 합한것도 같으면 다음조건. 사전순
                temp2 = [serials[l],serials[h]]
                temp2.sort()
                temp.append(temp2[0])
                if temp2[0] == serials[l]:
                    l+=1
                else:
                    h+=1

    while l < mid:
        temp.append(serials[l])
        l += 1

    while h < high:
        temp.append(serials[h])
        h += 1

    for i in range(low,high):
        serials[i] = temp[i-low]

    # print('정렬 후', serials)

serials = []

for _ in range(N):
    serials.append(input())

merge_sort(0,len(serials))

for serial in serials:
    print(serial)
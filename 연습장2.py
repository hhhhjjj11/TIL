import re

N = int(input())

def merge_sort(low, high):

    if high-low < 2:
        return

    mid = (low + high)//2

    merge_sort(low, mid)
    merge_sort(mid, high)

    temp = []

    l, h = low, mid

    while l < mid and h < high:
        if len(serials[l]) < len(serials[h]):
            temp.append(serials[l])
            l += 1
        elif len(serials[l]) > len(serials[h]):
            temp.append(serials[h])
            h += 1
        # 길이가 같으면 다음 조건으로 넘어가야 함
        elif len(serials[l]) == len(serials[h]):
            # 숫자를 더한다..
            numbers1 = re.sub(r'[^0-9]', '', serials[l])
            numbers
    while l < mid:
        temp.append(serials[l])
        l += 1

    while h < high:
        temp.append(serials[h])
        h += 1

    for i in range(low,high):
        serials[i] = temp[i-low]


serials = []

for _ in range(N):
    serials.append(input())

merge_sort(serials)

for serial in serials:
    print(serial)
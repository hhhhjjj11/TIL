# 2진수 10진수로 바꾸기 7비트씩 끊어서.
arr = list(map(int,input()))

N = len(arr)

num = 0

for i in range(N):
    j = i % 7
    num += arr[i] * (2**(6-j))
    if j ==6 :
        print(num, end=' ')


# 16진수를 2진수로 바꾸기
# 16진수 숫자 하나는 2진수로 바꾸면 4자리 숫자가 된다는 점!

arr = input() # 16진수 수를 인풋으로 받아서

for x in arr:
    num = int(x,16)
    for j in range(3, -1, -1):
        bit = 1 if num &(1<<j) else 0
        print(bit, end= '')
    print(' ', end= '')

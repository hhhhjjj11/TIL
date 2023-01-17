s = int(input('숫자를 입력해주세요 : '))
res=0
while s>0:
    res+=s%10
    s=s//10
print(res)
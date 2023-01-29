N,X=map(int,input().split())
li = list(map(int,input().split()))
str1=''
for item in li:
    if item<X:
        str1+=str(item)+' '
str1.strip()
print(str1)
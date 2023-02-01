li = ['c=','c-','dz=','d-','lj','nj','s=','z=']

str = input()
cnt=0
for i in li:
    cnt+=str.count(i)
    str =str.replace(i,'.')
    

a = str.split('.')
b = ''.join(a)
cnt+=len(b)
print(cnt)
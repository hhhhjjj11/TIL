grain_lst = [('고구마',3000), ('감자',2000), ('옥수수',4500),('토란',1300)]

M=0
name=''
for index, item in enumerate(grain_lst):
    if item[1]>=M:
        M=item[1]
        name=item[0]

print(name)
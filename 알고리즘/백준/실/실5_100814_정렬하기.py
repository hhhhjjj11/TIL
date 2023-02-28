N = int(input())
users = []
for i in range(N):
    age,name =input().split()
    age=int(age)
    users.append((i,age,name))

# print(users)

users = sorted(users, key = lambda x: (x[1],x[0]))
for item in users:
    print(f'{item[1]} {item[2]}')


# 알아두기 : 문자열로된 숫자는 첫번째 자리만 가지고 대소관계 따짐.
#               그래서 sort로 정렬해도 원하는 대로 안됨.
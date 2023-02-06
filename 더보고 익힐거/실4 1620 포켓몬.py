from sys import stdin

N, M = map(int,input().split())

by_id = {}
by_name = {}

for i in range(1,N+1):
    pok = stdin.readline().rstrip()
    by_id[i] = pok
    by_name[pok] = i

# print(by_id)
# print(by_name)

for i in range(M):
    quiz = stdin.readline().rstrip()
    if quiz.isalpha() :
        print(by_name[quiz])
    else:
        print(by_id[int(quiz)])

# 알아두기 1. 리스트로 하면 시간 더걸림 딕셔너리 키로 찾으면 시간 복잡도 1
# 알아두기 2. 키값으로 검색해야 시간이 1임 따라서 번호가 키인경우랑 이름이 키인경우
# 두가지의 딕셔너리를 만들어놓고 사용하는 것이 빠름.
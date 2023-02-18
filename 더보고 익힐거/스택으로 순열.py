lst = [1,2,3,4]
n = 2

permutations = []
stack = [([x], [i]) for i, x in enumerate(lst)]  # 순열저장리스트, 인덱스리스트
print('초기상태 스택 :', stack)

while stack:
    per, idx_list = stack.pop()
    
    # n개를 모두 뽑은 경우 순열을 추가한 후 continue
    if len(per)==n:
        permutations.append(per)
        continue
        
    # n개를 뽑지않은경우
    for i in range(len(lst)):
        # 뽑은 인덱스리스트에 포함되지 않은 경우 추가
        if i not in idx_list:
            stack.append((per+[lst[i]], idx_list+[i]))

print('만들어진 순열리스트')
for p in sorted(permutations):
    print(p)
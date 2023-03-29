lst = [1,2,3,4]
n = 2

combinations = []
stack = [([x], i) for i, x in enumerate(lst)]  # 조합저장리스트, 마지막인덱스값
print('초기상태 스택 :', stack)

while stack:
    comb, last_idx = stack.pop()
    
    # n개를 모두 뽑은 경우 조합을 추가한 후 continue
    if len(comb)==n:
        combinations.append(comb)
        continue
    
    # n개를 뽑지않은경우 마지막인덱스+1부터 추가
    for i in range(last_idx+1, len(lst)):
        stack.append((comb+[lst[i]], i))
            
print('만들어진 조합리스트')
for p in sorted(combinations):
    print(p)
# DFS 순열

li = [1,2,3,4]

stack = []

1 - 2 - 3- 4 -5

stack = [[x] for x in li]

memo = [0]
while stack :
    per = stack.pop()
    if
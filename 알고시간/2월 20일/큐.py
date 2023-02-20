from collections import deque

def enqueue(data):
    global rear
    rear += 1
    queue[rear] = data

def dequeue():
    global front
    front += 1
    return queue[front]

queue = [0]*3
front = -1
rear = -1

# 적당한 크기의 리스트를 만들고
# 프론트와 rear를 이용하여 더하고 지운다(?)
print(dequeue())
print(dequeue())

if front != rear:
    print(dequeue())
if front != rear:
    print(dequeue())

q = []
q.append(10)
q.append(20)
q.append(30)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

q1 = deque()
q1.append(100)
q1.append(200)
q1.append(300)
print(q1.popleft())

# 원형큐의 경우
# rear와 front를 옮겨주만 그만.


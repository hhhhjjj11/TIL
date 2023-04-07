N = int(input())

tree = {}

for _ in range(N):
    
    parent, child1, child2 = input().split()
    temp = [0,0]
    
    if child1 != '.':
        temp[0] = child1
    if child2 != '.':
        temp[1] = child2
    
    tree[parent] = temp

#print('tree',tree)

def preorder_traverse(T):
    if T:
        list_pre.append(T)
        preorder_traverse(tree[T][0])
        preorder_traverse(tree[T][1])

def inorder_traverse(T):
    if T:
        inorder_traverse(tree[T][0])
        list_inorder.append(T)
        inorder_traverse(tree[T][1])

def postorder_traverse(T):
    if T:
        postorder_traverse(tree[T][0])
        postorder_traverse(tree[T][1])
        list_post.append(T)

list_pre = []
list_inorder = []
list_post = []

preorder_traverse('A')
inorder_traverse('A')
postorder_traverse('A')

print(''.join(list_pre))
print(''.join(list_inorder))
print(''.join(list_post))


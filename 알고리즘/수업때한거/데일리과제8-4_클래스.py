class Stack():
    def __init__(self, list):
        self.list=list

    def empty(self):
        if self.list ==[]:
            return True
        else:
            return False
    
    def top(self):
        return self.list[-1]
    
    def pop(self):
        if self.list == []:
            return None
        else:
            return self.list.pop()
    
    def push(self, what_to_add):
        self.list.append(what_to_add)

    def __repr__(self):
        print(self.list)


a=Stack([])
print(a.empty())
print(a.push('ddd'))
print(a.push('ddd2'))
print(a.top())
print(a.pop())
a.__repr__()
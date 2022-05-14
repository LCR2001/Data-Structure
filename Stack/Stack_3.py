# Stack 연습문제 05번
class Stack:
    def __init__(self):
        self.box=[]
    def push(self,item):
        self.box.append(item)
    def pop(self):
        return self.box.pop()
    def top(self):
        return self.box[-1]
    def size(self):
        return len(self.box)
    
def parenBalance(s:str):
    checker = Stack()
    for ch in s: 
        if ch == '(': 
            checker.push(ch)
        else: 
            if checker.size() != 0:
                checker.pop()
            else:
                return False
    if checker.size() != 0:
        return False
    else:
        return True
    
a1 = ['((()))', '(()()())', '((()))((()))', '()']
a2 = ['((()', '(()())))', '()))', '()))(()']

result1 = [parenBalance(i) for i in a1]
print(result1)

result2 = [parenBalance(i) for i in a2]
print(result2)

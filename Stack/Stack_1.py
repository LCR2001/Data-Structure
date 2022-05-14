# Stack 연습문제 02번
from LinkedList import *

class ListStack:
    def __init__(self):
        self.__stack = LinkedListStack()
        
    def push(self,x):
        self.__stack.insert(0,x)
    
    def pop(self):
        return self.__stack.pop(0)
        
    def top(self):
        if self.isEmpty(): 
            return None
        else:
            return self.__stack.get(0)
    
    def isEmpty(self) -> bool:
        return self.__stack.isEmpty()
        
    def popAll(self):
        self.__stack.clear()
        
    def printStack(self):
        print("Stack:")
        for i in range(len(self.__stack)):
            print('stack[',i, ']:', self.__stack.get[i])
            print(i)
            

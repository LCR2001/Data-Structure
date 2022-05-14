class LinkedStack:
    def __init__(self):
        self.__stack = []
    
    def push(self,newItem):
        self.__stack.insert(0,newItem)
    
    def pop(self):
        return self.__stack.pop(0)
    
    def top(self):
        if self.isEmpty():
            print("No element in stack")
            return None
        else:
            return self.__stack[0]
    def isEmpty(self):
        return not bool(self.__stack)
    
    def popAll(self):
        return self.__stack.clear()
    
    def printStack(self):
        print("Stack")
        for i in range(len(self.__stack)):
            print("stack[",i,"]:",self.__stack[i])
        print()
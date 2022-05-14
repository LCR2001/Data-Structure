# Stack 연습문제 03번  
from liststack import * 
class sentenceChecker:
    def __init__ (self):
        
        self.__stack = LinkedStack()
    def is_included(self,s):
        
        for i in range(len(s)):
            if s[i] == "$":
                break
            self.__stack.push(s[i])
        for j in range(i+1,len(s)):
            curr = s[j]
            if curr != self.__stack.pop():
                return False
        return self.__stack.isEmpty()
        
        
if __name__ == "__main__":
    s = "abc$cba"
    checker = sentenceChecker()
    rv = checker.is_included(s)
    if rv == True:
        print("included")
    else:
        print("not included") 
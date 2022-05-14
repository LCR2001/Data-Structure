## 스택 2개로 큐 1개
## inbox : enqueue할 공간 ex) 1-2-3-4
## outbox : inbox에서 dequeue해서 enqueue해놓을 공간 ex) 4-3-2-1
## outbox에서 다시 추출 ex) 1-2-3-4

from LinkedStack import LinkedStack
class Queue:
    def __init__(self):
        self.inbox = LinkedStack()
        self.outbox = LinkedStack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        self.swap_element(self.outbox,self.inbox)
        return self.inbox.pop()
    
    def swap_element(self,inbox,outbox):
        while not inbox.isEmpty():
            outbox.push(s.pop())

if __name__ == "__main__":
    que = Queue()
    que.enqueue(1)
    que.enqueue(3)        
    que.enqueue(2)        
            
    print(que.dequeue())
    print(que.dequeue())
    print(que.dequeue())
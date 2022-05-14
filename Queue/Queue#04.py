##큐 연습문제 04번 --> 큐 2개로 스택 1개
from linkedQueue import linkedQueue

class Stack:
    def __init__(self):
        self.main = linkedQueue()
        self.sub = linkedQueue()   #임시 큐 만들어놓기

    def push(self, x):
        self.main.enqueue(x)

    def pop(self):
        if self.main.isEmpty():
            return

        while len(self.main()) != 1:  # 메인 큐가 1개 남을 때까지 다른 값들은 임시(다른) 큐에 넣어두기
            self.sub.put(self.main.get())

        result = self.main.get()

        self.main, self.sub = self.sub, self.main  
        return result

if __name__ == "__main__" :
    s = Stack()
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  
    print(s.pop())  
## 작성 덜 됐음.

from listNode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.__tail = ListNode("dummy", None)
        self.__tail.next = self.__tail
        self.__numItems = 0

    def insert(self, i:int, newItem) -> None:
        if (i>=0 and i <= self.__numItems):
            prev = self.getNode(i-1)
            newNode = ListNode(newItem, prev.next)
            prev.next = newNode
            if i== self.__numItems:
                self.__tail = newNode
            self.__numItems += 1

        else:
            print("index", i, ":out of bound in insert()")
    def append(self, newItem) -> None:
        newNode = ListNode(newItem, self.__tail.next)
        self.__tail.next = newNode
        self.__tail = newNode
        self.__numItems += 1

    def pop(self, *args):
        if self.isEmpty():
            return None

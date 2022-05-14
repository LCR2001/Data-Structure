class Heap:
    def __init__(self, list):
        if list == None:
            self.__A = []
        else:
            self.__A = list

    def insert(self,x):
       self.__A.append(x)
       self.__percolateUp(len(self.__A)-1)
            
    def __percolateUp(self,i:int):
        parent = (i -1) // 2
        if i>0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.__percolateUp(parent)
            
    def deleteMax(self):
        if (not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.__percolateDown(0)
            return max
        else:
            return None
        
    def __percolateDown(self, i:int):
    
        child = 2 * i + 1
        right = 2 * i + 2
        if (child <= len(self.__A)-1):
            if (right <= len(self.__A)-1 and self.__A[child] < self.__A[right]):
               child = right
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.__percolateDown(child)
            
            
    def max(self):
        return self.__A[0]
    
    def buildHeap(self):
        for i in range((len(self.__A)-2) // 2, -1, -1):
            self.__percolateDown(i)
        
            
    def isEmpty(self) -> bool:
        return len(self.__A) == 0
    
        #if (len(self)==0):
        #     return True
        # else:
        #     return False
    
    def clear(self):
        self.__A = []
        
    def size(self) : 
        return len(self.__A)
    
    def heapPrint(self):
        n = len(self.__A) 
        for i in range(1,2**1,1):
            if i <= n:
                print(self.__A[i-1], end= '')
            print(sep='\n\n')
        for i in range(2,2**2,1):
                if i<=n:
                    print(self.__A[i-1], end='')
        print(sep='\n\n')
        for i in range(4,2**3,1):
                if i<=n:
                    print(self.__A[i-1], end='')
        print(sep='\n\n')
        for i in range(8,2**4,1):
                if i<n:
                    print(self.__A[i-1], end='')
        print(sep='\n\n')
                    
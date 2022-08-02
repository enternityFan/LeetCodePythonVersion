# @Time : 2022-08-02 8:25
# @Author : Phalange
# @File : 622. 设计循环队列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [0] * k
        self.pushi = 0
        self.polli = 0
        self.size = 0
        self.limit = k


    def enQueue(self, value: int) -> bool:
        if self.size == self.limit:
            return False
        self.size +=1
        self.arr[self.pushi] = value
        self.pushi = self.pushi + 1 if self.pushi < self.limit-1 else 0
        return True


    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.size -=1
        ans = self.arr[self.polli]
        self.polli = self.polli +1 if self.polli < self.limit - 1 else 0
        return True


    def Front(self) -> int:
        if self.size == 0:
            return -1
        return self.arr[self.polli]


    def Rear(self) -> int:
        if self.size == 0:
            return -1

        return self.arr[self.pushi-1 if self.pushi -1 >=0 else self.limit-1]


    def isEmpty(self) -> bool:
        return self.size == 0


    def isFull(self) -> bool:
        return self.size == self.limit


arr = MyCircularQueue(3)
arr.enQueue(1)
arr.enQueue(2)
arr.enQueue(3)
arr.enQueue(4)
print(arr.Rear())
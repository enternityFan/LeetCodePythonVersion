# @Time : 2022-08-02 8:40
# @Author : Phalange
# @File : 641. 设计循环双端队列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class MyCircularDeque:

    def __init__(self, k: int):
        self.arr = [0] * (k+1)
        self.pushi = 0
        self.polli = 0
        self.limit = k + 1




    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.polli = (self.polli -1 + self.limit) % self.limit
        self.arr[self.polli] = value
        return True



    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.arr[self.pushi] = value
        self.pushi = (self.pushi + 1) % self.limit
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.polli = (self.polli + 1) % self.limit

        return True



    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.pushi = (self.pushi - 1 + self.limit) % self.limit

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[self.polli]


    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.arr[(self.pushi-1 + self.limit) % self.limit]

    def isEmpty(self) -> bool:
        if self.pushi == self.polli:
            return True
        return False


    def isFull(self) -> bool:
        if (self.pushi + 1) % self.limit == self.polli:
            return True
        return False



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()




arr = MyCircularDeque(3)
arr.insertLast(1)
arr.insertLast(2)
arr.insertFront(3)
arr.insertFront(4)
print(arr.getRear())
print(arr.isFull())
print(arr.deleteLast())
print(arr.insertFront(4))
print(arr.getFront())

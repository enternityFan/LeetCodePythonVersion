# @Time : 2022-08-02 10:25
# @Author : Phalange
# @File : 1823. 找出游戏的获胜者.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        self.arr = collections.deque(list(range(1,n+1)))
        while len(self.arr) !=1:

            for i in range(k-1):
                self.arr.append(self.arr.popleft())
            self.arr.popleft()




        return self.arr.pop()


arr = collections.deque([1,2,3,4])

print(arr.pop())
print(arr.popleft())
print(arr.append(3))
print(arr)
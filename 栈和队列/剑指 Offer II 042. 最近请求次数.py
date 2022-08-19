# @Time : 2022-08-19 10:29
# @Author : Phalange
# @File : 剑指 Offer II 042. 最近请求次数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class RecentCounter:

    def __init__(self):
        self.myque = collections.deque()

    def ping(self, t: int) -> int:
        if len(self.myque) >0 and t - self.myque[0] >3000:
            self.myque.popleft()
            while len(self.myque) >0 and t - self.myque[0] > 3000:
                self.myque.popleft()
        self.myque.append(t)
        return len(self.myque)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(435))
print(obj.ping(3573))
print(obj.ping(4015))
print(obj.ping(4918))
print(obj.ping(5098))


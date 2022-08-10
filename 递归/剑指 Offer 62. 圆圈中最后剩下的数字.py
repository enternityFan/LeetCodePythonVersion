# @Time : 2022-08-10 17:10
# @Author : Phalange
# @File : 剑指 Offer 62. 圆圈中最后剩下的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def f(self,n,m):
        if n ==0:
            return 0
        x = self.f(n-1,m)
        return (m + x) %n

    def lastRemaining(self, n: int, m: int) -> int:
        return self.f(n,m)





print(Solution().lastRemaining(5,3))


class Solution:

    def lastRemaining(self, n: int, m: int) -> int:
        """
        我自己写的，超时
        :param n:
        :param m:
        :return:
        """
        def f(arr:List,idx:int):
            if len(arr) == 1:
                return
            idx = (idx + m%len(arr) - 1) % len(arr)
            arr.pop(idx)
            f(arr,idx)

        mylist = list(range(n))
        f(mylist,0)
        return mylist[0]
# @Time : 2022-09-18 12:35
# @Author : Phalange
# @File : 202. 快乐数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def isHappy(self, n: int) -> bool:
        """
        对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
    然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
    如果这个过程 结果为1那么这个数就是快乐数。

        """

        def func(num):
            num = [int(c) * int(c) for c in str(num)]
            ans = sum(num)
            return ans

        prev = set()

        while n and n not in prev:
            prev.add(n)
            n = func(n)
            print(n)
            if n == 1:
                return True


        return False
print(Solution().isHappy(2))
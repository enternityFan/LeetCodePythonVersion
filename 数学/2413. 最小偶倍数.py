# @Time : 2022-10-02 12:13
# @Author : Phalange
# @File : 2413. 最小偶倍数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        return n*2
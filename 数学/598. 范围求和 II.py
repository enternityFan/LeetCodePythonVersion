# @Time : 2022-07-29 19:59
# @Author : Phalange
# @File : 598. 范围求和 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mina,minb = m,n
        for a,b in ops:
            mina = min(mina,a)
            minb = min(minb,b)

        return mina * minb

s = Solution()
print(s.maxCount(40000,40000,[]))
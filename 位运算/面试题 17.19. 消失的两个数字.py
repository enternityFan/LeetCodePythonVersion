# @Time : 2022-09-26 12:12
# @Author : Phalange
# @File : 面试题 17.19. 消失的两个数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
   """
   a + b = c
   a * b = d
   a * (c - a) = d
   """
   def missingTwo(self, nums: List[int]) -> List[int]:
        x = 0
        n = len(nums)

        for a in nums:
            x ^= a

        for b in range(1, n + 2 + 1):
            x ^= b


        lb = x & (-x)

        y = 0
        for a in nums:
            if a & lb:
                y ^= a

        for b in range(1, n + 2 + 1):
            if b & lb:
                y ^= b

        return [y, y ^ x]


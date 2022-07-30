# @Time : 2022-07-29 14:43
# @Author : Phalange
# @File : 384. 打乱数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
import random

"""
暴力的解法
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums



    def shuffle(self) -> List[int]:
        shuffled = [0] * len(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums

"""
Fisher-Yates 洗牌算法
"""

class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums



    def shuffle(self) -> List[int]:

        for i in range(len(self.nums)):
            j = random.randrange(i,len(self.nums))
            self.nums[j],self.nums[i] = self.nums[i],self.nums[j]

        return self.nums
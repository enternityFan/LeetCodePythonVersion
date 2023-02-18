#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：384. 打乱数组.py
@Author ：HuntingGame
@Date ：2023-02-10 8:12 
C'est la vie!!! enjoy ur day :D
'''
from random import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        """
        总的来说，还是很简单的。
        :param nums:
        """
        self.origin = nums.copy()
        self.N = len(nums)
        self.shuffled = [0] * self.N
        for i in range(N):
            self.shuffled[i] = self.origin[i]


    def reset(self) -> List[int]:
        return self.origin


    def shuffle(self) -> List[int]:
        for i in range(self.N-1,-1,-1):
            r = int(random.random() * (i+1))
            self.shuffled[r],self.shuffled[i] = self.shuffled[i],self.shuffled[r]

        return self.shuffled



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
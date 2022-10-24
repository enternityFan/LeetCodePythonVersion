#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/21 16:32
# @Author  : HuntingGame
# @FileName: 剑指 Offer II 004. 只出现一次的数字.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        mycnt = collections.Counter(nums)
        for key,val in mycnt.items():
            if val == 1:
                return key
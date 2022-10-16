#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/16 10:32
# @Author  : HuntingGame
# @FileName: 6205. 反转之后不同整数的数目.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 10:
                continue
            nums.append(int(str(nums[i])[::-1]))


        return len(set(nums))
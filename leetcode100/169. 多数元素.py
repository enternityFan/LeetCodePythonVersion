#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：169. 多数元素.py
@Author ：HuntingGame
@Date ：2023-02-07 19:48 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        水王问题，很有意思
        一次删除两个不同的数字，最后剩的那个没法再删的数，就是要求的解
        :param nums:
        :return:
        """
        cand,HP = 0,0
        for i in range(len(nums)):
            if HP == 0:
                cand = nums[i]
                HP = 1
            elif nums[i] == cand:
                HP +=1
            else:
                HP-=1

        return cand

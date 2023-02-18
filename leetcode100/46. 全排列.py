#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：46. 全排列.py
@Author ：HuntingGame
@Date ：2023-02-02 21:20 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        ans = []
        self.process(nums,0,ans)
        return ans

    def process(self,nums:List,idx:int,ans:List):

        if idx == len(nums):
            temp = [i for i in nums]
            ans.append(temp)

        else:
            for j in range(idx,len(nums)):
                num = nums[idx]
                nums[idx] = nums[j]
                nums[j] = num
                self.process(nums,idx+1,ans)
                num = nums[idx]
                nums[idx] = nums[j]
                nums[j] = num
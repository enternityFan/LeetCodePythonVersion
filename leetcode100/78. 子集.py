#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：78. 子集.py
@Author ：HuntingGame
@Date ：2023-02-03 17:42 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = []
        path = []
        self.process(nums,0,path,ans)

    def process(self,nums,idx,path,ans):
        """
        idx位置做决定，要或者不要。
        :param nums:
        :param idx:
        :param path:
        :param ans:
        :return:
        """
        if idx == len(nums):
            ans.append(copy.deepcopy(path))
        else:
            self.process(nums,idx+1,path,ans)
            path.append(nums[idx])
            self.process(nums,idx+1,path,ans)
            path.pop()



#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 082. 含有重复元素集合的组合.py
@Author ：HuntingGame
@Date ：2022-10-25 9:24 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
        self.tmpval = 0
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        还需要进行一些减枝的操作。

        :param candidates:
        :param target:
        :return:
        """
        candidates.sort()

        def process(idx,used,flag=0):
            if flag and self.tmpval == target:
                if self.tmp not in self.ans:
                    self.ans.append(self.tmp[:])
                return
            if idx == len(candidates):
                return
            if self.tmpval > target:
                return


            process(idx+1,used)
            self.tmp.append(candidates[idx])
            self.tmpval +=candidates[idx]
            process(idx+1,used,flag=1)
            self.tmp.pop()
            self.tmpval -=candidates[idx]

        process(0,set())
        return self.ans
candidates = [2,5,2,1,2]
target = 5
print(Solution().combinationSum2(candidates,target))
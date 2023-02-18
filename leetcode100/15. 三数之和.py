#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：15. 三数之和.py
@Author ：HuntingGame
@Date ：2023-02-01 20:15 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    """
    这是第一个解题的思路，就是正着遍历，但是这样不好，因为有一个数组的insert插入；
    那么第二个思路就是倒着遍历，就不用insert了。见下面的代码
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if i==0 or nums[i-1] !=nums[i]:
                nexts = self.twoSum(nums,i + 1,-nums[i])
                for cur in nexts:
                    cur.insert(0,nums[i])
                    ans.append(cur)
        return ans
    def twoSum(self,nums,begin,target):
        L = begin
        R = len(nums) - 1
        ans = []
        while L < R:
            if nums[L] + nums[R] > target:
                R -=1
            elif nums[L] + nums[R] < target:
                L +=1
            else:
                if L == begin or nums[L-1]!=nums[L]:
                    ans.append([nums[L],nums[R]])
                L+=1
        return ans

class Solution:
    """
    这是第二个解题的思路，就是到着遍历。
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)-1,1,-1):
            if i==len(nums)-1 or nums[i] !=nums[i+1]:
                nexts = self.twoSum(nums,i-1,-nums[i])
                for cur in nexts:
                    cur.append(nums[i])
                    ans.append(cur)
        return ans
    def twoSum(self,nums,end,target):
        L = 0
        R = end
        ans = []
        while L < R:
            if nums[L] + nums[R] > target:
                R -=1
            elif nums[L] + nums[R] < target:
                L +=1
            else:
                if L == 0 or nums[L-1]!=nums[L]:
                    ans.append([nums[L],nums[R]])
                L+=1
        return ans
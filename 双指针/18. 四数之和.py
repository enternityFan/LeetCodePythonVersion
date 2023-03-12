#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：18. 四数之和.py
@Author ：HuntingGame
@Date ：2023-03-12 11:56 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        if n < 4:
            return ans
        print(nums)
        for d in range(3,n):
            print("nums[d]=",nums[d])
            next = self.threeSum(nums,d,target - nums[d])
            print("next=",next)
            for each in next:
                if nums[each[-1]] !=nums[d]:
                    each.append(nums[d])
                    ans.append(each)


        return ans

    def threeSum(self,nums,end,target):
        ans = []
        for c in range(2,end):
            next = self.twoSum(nums,c-1,target-nums[c])
            print("next3=",next)
            for each in next:
                if nums[each[-1]] !=nums[c]:
                    each.append(nums[c])
                    ans.append(each)



        return ans

    def twoSum(self,nums,end,target):
        ans = []
        L = 0
        R = end
        #print(end,target)
        while L < R:
            if (L == 0 or nums[L] != nums[L-1]) and nums[L] + nums[R] == target:

                ans.append([nums[L],nums[R]])
                L +=1
            elif nums[L] + nums[R] > target:
                R -=1
            elif nums[L] + nums[R] < target:
                L +=1
            else:
                L +=1
        return ans

nums = [1,0,-1,0,-2,2]
nums = [2,2,2,2,2]
print(Solution().fourSum(nums,8))
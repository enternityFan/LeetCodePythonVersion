#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：268. 丢失的数字.py
@Author ：HuntingGame
@Date ：2023-02-08 13:29 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        l左侧的位置，都可以保证nums[i] = i
        r位置表示缺失的最小的数往大了预计,他的右边是垃圾区
        :param nums:
        :return:
        """
        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == l:
                l +=1
            elif nums[l] < l or nums[l] >= r or nums[nums[l]] == nums[l]:
                #以上三种情况，都说明这个数是没有用的
                #和r-1的位置交换，然后再扩一下垃圾区。
                r -=1
                nums[l],nums[r] = nums[r],nums[l]
            else:
                tmp = nums[l]

                nums[l]=nums[nums[l]]
                nums[tmp] = tmp


        return l

print(Solution().missingNumber([3,0,1]))










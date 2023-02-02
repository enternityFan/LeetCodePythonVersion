#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：26. 删除有序数组中的重复项.py
@Author ：HuntingGame
@Date ：2023-02-02 9:44 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        两个指针，一个done指针，他前面的都是放好的区域，cur是当前的指针，如果cur和done指针比（因为是有序的）不一样，那就和done指针后面的交换，
        然后done指针后移一位，cur后移，如果不一样，那就只cur后移。到最后，done指针之前的就是答案

        这个题其实一个指针也是可以的
        :param nums:

        :return:
        """
        done = 0
        if len(nums) == 1:
            return 1

        for i in range(1,len(nums)):
            if nums[i] != nums[done]:
                nums[done+1],nums[i] = nums[i],nums[done+1]
                done +=1
        print(nums)
        return done+1

print(Solution().removeDuplicates([1,1,2]))







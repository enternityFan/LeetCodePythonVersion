#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：88. 合并两个有序数组.py
@Author ：HuntingGame
@Date ：2023-02-03 18:52 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx = len(nums1)#从后往前填，谁大谁填这里
        while m > 0 and n > 0:
            if nums1[m - 1] >=nums2[n - 1]:
                nums1[idx-1] = nums1[m-1]
                idx -=1
                m -=1
            else:
                nums1[idx-1] = nums2[n-1]
                idx -=1
                n -=1

        while m > 0:
            nums1[idx-1] = nums2[m-1]
            idx -=1
            m -=1

        while n > 0:
            nums2[idx-1] = nums2[n-1]
            n -=1
            idx -=1


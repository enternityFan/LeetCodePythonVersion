#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：454. 四数相加 II.py
@Author ：HuntingGame
@Date ：2023-02-09 14:18 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        mymap = {}
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                tmp = nums1[i] + nums2[j]
                if tmp not in mymap:
                    mymap[tmp] = 1
                else:
                    mymap[tmp]+=1
        ans = 0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                tmp = nums3[i] + nums4[j]
                if -tmp in mymap:
                    ans +=mymap[-tmp]
        return ans
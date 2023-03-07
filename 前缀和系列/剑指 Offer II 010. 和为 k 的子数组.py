#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：剑指 Offer II 010. 和为 k 的子数组.py
@Author ：HuntingGame
@Date ：2023-03-07 11:49 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mydict = {}  #以i位置为结尾的前缀和:i
        mydict2 = {}# i:以i位置为结尾的前缀和
        tmp = 0
        for i in range(len(nums)):

            mydict2[i] = tmp
            mydict[tmp] = i
            tmp += nums[i]

        ans = 0
        for i in range(len(nums)):
            # if k - nums[i] in mydict and i !=mydict[k-nums[i]]:
            #     print(i,mydict[k-nums[i]])
            #     ans +=1
            for j in range(i):
                if k == nums[i] + mydict2[i] - mydict2[j] :
                    print(i,j)
                    ans +=1
                elif mydict2[i] - mydict2[j] < k:
                    break
        return ans

print(Solution().subarraySum([1,2,1,2,1],3))
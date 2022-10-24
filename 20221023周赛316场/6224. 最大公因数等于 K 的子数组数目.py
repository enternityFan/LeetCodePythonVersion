#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/23 10:36
# @Author  : HuntingGame
# @FileName: 6224. 最大公因数等于 K 的子数组数目.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        ans = 0
        for i in range(n):
            if nums[i] % k == 0:
                dp[i] = 1
        conts = [] # 连续数组的长度
        flag = 0
        length = 0
        for i in range(n):
            if dp[i] == 1:
                ans +=1
                flag +=1
            elif flag >1 :
                conts.append(flag)
                flag = 0
        if flag > 1:
            conts.append(flag)
            flag = 0
        print(conts)
        for each in conts:
            ans +=(each-1)*each //2





        return ans
nums = [9,3,1,2,6,3]
k = 3
print(Solution().subarrayGCD(nums,k))
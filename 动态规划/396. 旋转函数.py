#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2023/2/20 12:34
# @Author  : HuntingGame
# @FileName: 396. 旋转函数.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
import collections
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        首先，用暴力尝试来做。
        做一个双端队列，来模拟旋转的操作。
        :param nums:
        :return:
        """
        deque = collections.deque(nums)
        ans = 0
        dp = [0] * len(nums)

        for i in range(len(nums)):
            dp[0] +=nums[i] * i
        n = len(nums)
        sumnum = sum(nums)
        ans = dp[0]
        for i in range(1,n):

            dp[i] = dp[i-1] +sumnum - nums[n-i] * n

            ans = max(dp[i],ans)


        return ans


print(Solution().maxRotateFunction([4,3,2,6]))








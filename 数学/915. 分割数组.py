#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/10/24 21:33
# @Author  : HuntingGame
# @FileName: 915. 分割数组.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        left_big = [0] * n  # 左到右，每个位置对应的最大的
        right_small = [0] * n  # 从右到左，每个位置对应的最小的
        left_big[0] = nums[0]
        right_small[-1] = 1000005
        for i in range(1, n):

            if nums[i] > left_big[i - 1]:
                left_big[i] = nums[i]
            else:
                left_big[i] = left_big[i - 1]

        for i in range(n - 2, -1, -1):
            if nums[i] > right_small[i + 1]:
                right_small[i] = right_small[i + 1]
            else:
                right_small[i] = nums[i]

        ans = 0
        for i in range(n - 1):
            if left_big[i] <= right_small[i + 1]:
                ans = i + 1
                break
        return ans



print(Solution().partitionDisjoint([5,0,3,8,6]))



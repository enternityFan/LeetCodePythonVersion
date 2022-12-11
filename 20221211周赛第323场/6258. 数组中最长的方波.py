#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2022/12/11 10:40
# @Author  : HuntingGame
# @FileName: 6258. 数组中最长的方波.py
# @Software: PyCharm
# C'est la vie. Enjoy ur day ! :D
from typing import List


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # 排序加二分
        nums.sort()
        # 二分
        ans = -1
        n = len(nums)

        for i in range(1,n):
            target = nums[i-1] ** 2 # 子序列的第2个值
            if n-i <= ans:
                break
            length = 1  # 子序列的长度
            flag = 0 # 表示没有找到
            while flag or target == nums[i-1] **2:
                l = i
                r = n - 1

                flag = 0  # 表示没有找到
                while l <=r:
                    mid = l + ((r - l) >> 1)
                    if nums[mid] == target:
                        flag = 1
                        target = target ** 2
                        length +=1
                        break
                    elif nums[mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1
                if not flag:
                    break
            if length > 1:
                ans = max(ans,length)
        return ans

print(Solution().longestSquareStreak([4,3,6,16,8,2]))
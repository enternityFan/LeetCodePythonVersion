#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@Project ：LeetCodePthonVersion 
@File ：41. 缺失的第一个正数.py
@Author ：HuntingGame
@Date ：2023-02-02 13:26 
C'est la vie!!! enjoy ur day :D
'''
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        做一个L，R的变量，L指向0，R指向len(nums)；
        1）0到L-1的位置都做到了i位置是i+1,所以一开始就是0到-1的位置做到了，因为我们还没看，所以是无效的；
        2)R表示你没有看过的部分最优预期缺的尽可能大的最小值，所以开始要指向len(nums)，也就是说，nums一个数都不缺，那肯定len(nums)就是没看过最优预期的尽可能大的最小值的。
        那么有以下的情况：
        1.如果预期是1到R，当前数字大于R，那么就最好预期变差，那就交换，R--
        2.如果满足i位置是i+1,那就L++
        3.如果i位置是小于等于L的，那就也和R的交换，R--
        4.L位置的V应该放在V-1的位置上，而V-1上已经是V了，那么此时就也要和R交换，R--
        当L和R相遇的时候就知道缺谁了。

        :param nums:
        :return:
        """

        l = 0
        r = len(nums)
        while l < r:
            if nums[l] == l+1:
                l+=1
            elif nums[l] <= l or nums[l] > r or nums[nums[l] - 1] == nums[l]:# 最后一个条件其实就是说V的那个情况
                nums[l] = nums[r-1]
                r -=1
            else:
                temp = nums[nums[l] -1]
                nums[nums[l]-1] = nums[l]
                nums[l] = temp

        return l + 1

print(Solution().firstMissingPositive([2,1]))


















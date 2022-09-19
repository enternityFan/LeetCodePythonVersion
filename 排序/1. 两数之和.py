# @Time : 2022-09-19 12:11
# @Author : Phalange
# @File : 1. 两数之和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtab = {}
        ans = []
        for i,num in enumerate(nums):
            if target - num in hashtab:
                ans = [i,hashtab[target-num]]
                break
            hashtab[num] = i

        return ans

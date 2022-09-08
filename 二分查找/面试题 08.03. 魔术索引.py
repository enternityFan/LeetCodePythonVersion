# @Time : 2022-09-08 20:17
# @Author : Phalange
# @File : 面试题 08.03. 魔术索引.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:

        if not nums:
            return -1
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == i:
                return i
            if nums[i] > i:
                i = nums[i]
            else:
                i = i +1
        return -1

print(Solution().findMagicIndex([0,0,2]))
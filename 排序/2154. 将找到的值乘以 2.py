# @Time : 2022-07-29 21:13
# @Author : Phalange
# @File : 2154. 将找到的值乘以 2.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums = sorted(nums)
        for each in nums:
            if each ==original:
                original = original * 2
        return original
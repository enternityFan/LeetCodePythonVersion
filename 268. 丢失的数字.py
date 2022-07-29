# @Time : 2022-07-29 16:28
# @Author : Phalange
# @File : 268. 丢失的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        sn = set(nums)
        return int(len(nums)*(len(nums)+1)/2 - sum(sn))

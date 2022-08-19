# @Time : 2022-08-19 10:54
# @Author : Phalange
# @File : 剑指 Offer 53 - II. 0～n-1中缺失的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return (n+1)*n//2 - sum(nums)
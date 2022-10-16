# @Time : 2022-10-14 8:37
# @Author : Phalange
# @File : 2149. 按符号重排数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        p1 = 0
        p2 = 0
        for i in range(n):
            if nums[i] > 0:
                nums[p1] = nums[i]
                p1 +=2
            else:
                nums[p2] = nums[i]
                p2 +=2
        return ans

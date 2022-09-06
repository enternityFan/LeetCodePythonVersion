# @Time : 2022-09-06 19:27
# @Author : Phalange
# @File : 1470. 重新排列数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[i+n])

        return ans

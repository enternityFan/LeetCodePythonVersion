# @Time : 2022-08-10 21:08
# @Author : Phalange
# @File : 1389. 按既定顺序创建目标数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            ans.insert(index[i],nums[i])

        return ans
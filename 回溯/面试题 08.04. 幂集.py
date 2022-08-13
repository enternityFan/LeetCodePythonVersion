# @Time : 2022-08-13 16:04
# @Author : Phalange
# @File : 面试题 08.04. 幂集.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def process(idx):
            if idx == len(nums):
                ans.append(tmp[:])
                return

            process(idx+1)
            tmp.append(nums[idx])
            process(idx+1)
            tmp.pop()

        process(0)

        return ans



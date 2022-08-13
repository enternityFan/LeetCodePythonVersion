# @Time : 2022-08-13 16:22
# @Author : Phalange
# @File : 78. 子集.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        tmp = []
        def dfs(idx):
            if idx == len(nums):
                ans.append(tmp[:])
                return

            dfs(idx+1)
            tmp.append(nums[idx])
            dfs(idx+1)
            tmp.pop()

        dfs(0)
        return ans
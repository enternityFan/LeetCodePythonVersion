# @Time : 2022-08-13 17:15
# @Author : Phalange
# @File : 46. 全排列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def process(idx):
            if idx == len(nums):
                ans.append(nums[:])
                return

            for i in range(idx,len(nums)):
                nums[i],nums[idx] = nums[idx],nums[i]
                process(idx+1)
                nums[i],nums[idx] = nums[idx],nums[i]

        process(0)
        return ans

print(Solution().permute([1,2,3]))
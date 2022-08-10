# @Time : 2022-08-10 20:17
# @Author : Phalange
# @File : 剑指 Offer II 083. 没有重复元素集合的全排列.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.f(nums,0)

        return self.ans

    def f(self,nums,idx):
        if idx == len(nums):
            self.ans.append(nums[:])
            return


        for i in range(idx,len(nums)):


            nums[i],nums[idx] = nums[idx],nums[i]
            self.f(nums,idx+1)
            nums[i], nums[idx] = nums[idx], nums[i]



print(Solution().permute([1,2,3]))
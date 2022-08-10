# @Time : 2022-08-10 20:46
# @Author : Phalange
# @File : 47. 全排列 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:

    def __init__(self):
        self.ans = []


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:


        self.f(nums,0)
        return self.ans



    def f(self,nums,idx):
        if idx == len(nums):
            self.ans.append(nums[:])
            return

        visit = [0] * 20
        for i in range(idx,len(nums)):
            if visit[nums[i]+10] == 0:
                visit[nums[i]+10] = 1

                nums[i],nums[idx] = nums[idx],nums[i]

                self.f(nums,idx+1)

                nums[i],nums[idx] = nums[idx],nums[i]

print(Solution().permuteUnique([1,1,2]))
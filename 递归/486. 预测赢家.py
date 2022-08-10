# @Time : 2022-08-10 17:37
# @Author : Phalange
# @File : 486. 预测赢家.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        a = self.f(nums,0,len(nums)-1)
        b =self.s(nums,0,len(nums)-1)
        if a >=sum(nums) - a:
            return True
        return False,a,b




    def f(self,nums,L,R):
        if L==R:
            return nums[L]


        return max(nums[L] + self.s(nums,L+1,R),nums[R] + self.s(nums,L,R-1))

    def s(self,nums,L,R):
        if L == R:
            return nums[L]
        return min(self.f(nums,L+1,R),self.f(nums,L,R-1))

print(Solution().PredictTheWinner([1,5,2,4,6]))
# @Time : 2022-09-08 21:30
# @Author : Phalange
# @File : 238. 除自身以外数组的乘积.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward = [1] * n
        backward = [1] * n
        for i in range(1,n):
            forward[i] = forward[i-1] * nums[i-1]

        for i in range(n-2,-1,-1):
            backward[i] = backward[i+1] * nums[i+1]


        print(backward)
        print(forward)
        for i in range(n):
            forward[i] *=backward[i]



        return  forward



print(Solution().productExceptSelf([1,2,3,4]))
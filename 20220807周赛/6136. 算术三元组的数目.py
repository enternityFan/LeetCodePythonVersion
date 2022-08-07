# @Time : 2022-08-07 10:30
# @Author : Phalange
# @File : 6136. 算术三元组的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):

            for j in range(i+1,n):
                if nums[j] - nums[i] == diff:
                    for k in range(j+1,n):
                        if nums[k] - nums[j] == diff:
                            ans +=1
        return ans
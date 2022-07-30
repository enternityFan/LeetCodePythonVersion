# @Time : 2022-07-27 17:13
# @Author : Phalange
# @File : 724. 寻找数组的中心下标.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        P = [0] * len(nums)
        idx = -1
        l = len(P)
        P[l-1] = sum(nums) - nums[l-1]
        for i in range(len(nums)):
            P[i] = sum(nums[:i])

            if P[i] == P[l - 1] - P[i] -nums[i] + nums[l-1]:
                idx = i
                break

        return idx


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        idx = -1
        num = sum(nums)
        for i in range(len(nums)):
            if sum(nums[:i]) * 2  + nums[i] == num:
                idx = i
                break

        return idx






s = Solution()
nums = [1, 7, 3, 6, 5, 6]
nums2 = [1,2,3]
nums3 = [2,1,-1]
print(s.pivotIndex(nums))
print(s.pivotIndex(nums2))
print(s.pivotIndex(nums3))
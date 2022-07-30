# @Time : 2022-07-30 17:21
# @Author : Phalange
# @File : 1365. 有多少小于当前数字的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

import collections
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums = list(enumerate(nums))
        nums = sorted(nums,key= lambda x:x[1])

        res = [0] * len(nums)
        for i in range(len(nums)):
            idx = i
            while idx !=-1 and nums[i][1] == nums[idx][1]:
                idx -=1
            res[nums[i][0]] = idx+1


        return res

s = Solution()
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))








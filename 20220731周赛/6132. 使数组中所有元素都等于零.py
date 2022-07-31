# @Time : 2022-07-31 10:31
# @Author : Phalange
# @File : 6132. 使数组中所有元素都等于零.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = sorted(nums)
        times =0
        for i in range(len(nums)):
            if nums[i] == 0:
                continue
            else:
                times +=1

                for j in range(i+1,len(nums)):
                    nums[j] -=nums[i]
                nums[i] = 0
        return times


print(Solution().minimumOperations([0]))
print(Solution().minimumOperations([1,5,0,3,5]))
print(Solution().minimumOperations([0,2,6,7]))
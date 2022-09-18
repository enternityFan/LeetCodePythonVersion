# @Time : 2022-09-15 13:20
# @Author : Phalange
# @File : 剑指 Offer II 007. 数组中和为 0 的三个数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        [-4,2,2,2]
        [3,0,-2,-1,1,2]
        -2 -1 0 1 2 3
        [-2,-1,3]
        [-1,0,1]

        :param nums:
        :return:
        """
        nums.sort()
        n = len(nums)
        ans = []
        for i in range(n):
            if i!=0 and nums[i-1] == nums[i]:
                continue
            if nums[i] > 0:
                return ans
            for j in range(i+1,n):
                if j !=i+1 and nums[j-1] == nums[j]:
                    continue
                if nums[i] + nums[j] > 0:
                    break
                for k in range(j+1,n):
                    if k!=j+1 and nums[k-1] == nums[k]:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans.append([nums[i],nums[j],nums[k]])
                    elif nums[i] + nums[j] + nums[k] > 0:
                        break

        return ans


print(Solution().threeSum([3,0,-2,-1,1,2]))
print(Solution().threeSum([-4,2,2,2]))

print(math.ceil(4.6))
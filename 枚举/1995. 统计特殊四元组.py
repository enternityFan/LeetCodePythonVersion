# @Time : 2022-08-13 17:46
# @Author : Phalange
# @File : 1995. 统计特殊四元组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for a in range(n):
            for b in range(a+1,n):
                for c in range(b+1,n):
                    for d in range(c+1,n):
                        if nums[a] + nums[b] + nums[c] == nums[d]:
                            ans +=1

        return ans


print(Solution().countQuadruplets([1,1,1,3,5]))
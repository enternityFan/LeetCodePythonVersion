# @Time : 2022-08-20 11:06
# @Author : Phalange
# @File : 1984. 学生分数的最小差值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        elif n == k:
            return max(nums) - min(nums)
        nums.sort()
        if k == 1:
            return 0
        ans = 1000000
        st = 0
        ed = k-1
        while ed < n:
            val = nums[ed] - nums[st]
            ans = min(ans,val)
            st+=1
            ed +=1
        return ans
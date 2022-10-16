# @Time : 2022-10-13 9:36
# @Author : Phalange
# @File : 1630. 等差子数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        lq = len(l)
        ans = []
        for i in range(lq):
            tmpnums = sorted(nums[l[i]:r[i]+1])
            flag = True
            pd = tmpnums[1] - tmpnums[0]
            d = pd
            for j in range(2,len(tmpnums)):
                d = tmpnums[j] - tmpnums[j-1]
                if d !=pd:
                    flag = False
                    break
            ans.append(flag)
        return ans
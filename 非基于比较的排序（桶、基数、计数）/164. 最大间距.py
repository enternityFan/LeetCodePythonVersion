# @Time : 2022-08-04 11:58
# @Author : Phalange
# @File : 164. 最大间距.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        help = [0] * len(nums)
        maxBit = self.getMaxBit(nums)
        for d in range(1,maxBit+1):

            count = [0] * 10
            for i in range(len(nums)):
                j = int((nums[i] / math.pow(10,d-1)) %(10))
                count[j] +=1

            for i in range(1,10):
                count[i] = count[i] + count[i-1]


            # 从右往左取
            for i in range(len(nums)-1,-1,-1):
                j = int((nums[i] / math.pow(10,d-1)) %(10))
                help[count[j]-1] = nums[i]
                count[j] -=1

            # 复制回去
            for i in range(len(nums)):
                nums[i] = help[i]

        err = 0
        for i in range(1,len(nums)):
            err = max(err,nums[i] - nums[i-1])

        return err
    def getMaxBit(self, nums):
        maxValue = max(nums)
        idx = 0
        while maxValue >0:
            maxValue //=10
            idx +=1
        return idx



print(Solution().maximumGap([1,1000000]))
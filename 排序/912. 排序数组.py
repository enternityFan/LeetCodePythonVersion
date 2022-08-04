# @Time : 2022-08-04 12:39
# @Author : Phalange
# @File : 912. 排序数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # 桶排序
        length = len(nums)
        help = [0]*length
        maxBit = self.getMaxBit(nums)
        for d in range(1,maxBit+1):
            count = [0] * 10
            for i in range(length):
                j = int(((nums[i]) / (math.pow(10,d-1)))%10) # 得到对应位数的值
                count[j] +=1
            for i in range(1,10):
                count[i] = count[i] + count[i-1]

            for i in range(length-1,-1,-1):
                j = int(((nums[i]) / (math.pow(10, d - 1))) % 10)  # 得到对应位数的值
                help[count[j]-1] = nums[i]
                count[j] -=1

            for i in range(length):
                nums[i] = help[i]

        return nums
    def getMaxBit(self, nums):
        maxValue = max(nums)
        idx = 0
        while maxValue>0:
            maxValue = maxValue // 10
            idx +=1
        return idx

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums,0,len(nums)-1)

        return nums

    def merge_sort(self, nums, L, R):
        if L == R:
            return
        mid = L + ((R - L ) >>1)
        self.merge_sort(nums,L,mid)
        self.merge_sort(nums,mid+1,R)
        help = []
        i,j = L,mid+1
        while i<=mid and j <=R:
            if nums[i] > nums[j]:
                help.append(nums[j])
                j+=1
            else:
                help.append(nums[i])
                i+=1
        while i <=mid:
            help.append(nums[i])
            i +=1
        while j <=R:
            help.append(nums[j])
            j +=1
        nums[L:R+1] = help



print(Solution().sortArray([5,2,3,1]))
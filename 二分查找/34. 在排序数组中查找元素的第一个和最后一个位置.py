# @Time : 2022-09-24 15:02
# @Author : Phalange
# @File : 34. 在排序数组中查找元素的第一个和最后一个位置.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        st,ed = -1,-1
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] >=target:
                r = mid
            else:
                l = mid + 1
        if nums[l] !=target:return [-1,-1]
        st = l
        l = 0


        while l < r:
            mid = l + ((r - l) >> 1)
            if nums[mid] <=target:
                l = mid + 1
            else:
                r = mid
        ed = l-1
        return [st,ed]






class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        st,ed = -1,-1
        n = len(nums)

        l = 0
        r = n-1
        while l <= r:
            mid = l + ((r-l) >> 1)
            if nums[mid] <target:
                r = mid - 1
            elif nums[mid] >target:
                l = mid + 1
            else:
                st = min(mid,st)
                ed = max(ed,mid)





        return [st,ed]



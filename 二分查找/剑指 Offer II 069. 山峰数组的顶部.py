# @Time : 2022-08-04 20:53
# @Author : Phalange
# @File : 剑指 Offer II 069. 山峰数组的顶部.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        l = 0
        r = len(arr)-1
        ans = 0
        while l <=r:
            mid = l + ((r-l)>>1)
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                ans = mid
                break
            elif arr[mid] > arr[mid+1]:
                r = mid - 1
            else:
                l = mid + 1
        return ans

print(Solution().peakIndexInMountainArray(
[24,69,100,99,79,78,67,36,26,19]))
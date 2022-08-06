# @Time : 2022-08-05 18:38
# @Author : Phalange
# @File : 704. 二分查找.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ans = -1
        l = 0
        r = len(nums)-1
        while l <=r:
            mid = l + ((r-l) >> 1)
            if nums[mid] == target:
                ans = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return ans
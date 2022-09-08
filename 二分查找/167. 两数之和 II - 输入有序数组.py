# @Time : 2022-09-08 20:39
# @Author : Phalange
# @File : 167. 两数之和 II - 输入有序数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)
        for i in range(n):
            l = i+1
            r = n - 1
            while l <=r:
                mid = l + ((r - l) >> 1)
                if numbers[mid] == target - numbers[i]:
                    return [i,mid]
                elif numbers[mid] > target - numbers[i]:
                    r = mid - 1
                else:
                    l = mid + 1
        return [-1,-1]



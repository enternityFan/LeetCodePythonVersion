# @Time : 2022-09-05 19:04
# @Author : Phalange
# @File : 1295. 统计位数为偶数的数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for each in nums:
            tmp = [c for c in str(each)]
            if len(tmp) % 2 == 0:
                ans +=1

        return ans

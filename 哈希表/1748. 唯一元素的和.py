# @Time : 2022-08-20 17:28
# @Author : Phalange
# @File : 1748. 唯一元素的和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        mymap = collections.Counter(nums)
        ans = 0
        for key,val in mymap.items():
            if val ==1:
                ans +=key
        return ans
# @Time : 2022-09-20 21:24
# @Author : Phalange
# @File : 128. 最长连续序列2.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        [1,3,2]
        1: 1
        3: 3
        2:：2
        :param nums:
        :return:
        """
        mydict ={}
        n = len(nums)
        for i in range(n):
            mydict[nums[i]] = 1
            if nums[i]-1 in mydict:
                mydict[nums[i]]= mydict[nums[i]-1] + 1




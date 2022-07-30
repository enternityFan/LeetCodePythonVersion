# @Time : 2022-07-29 20:28
# @Author : Phalange
# @File : 1512. 好数对的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    count +=1



        return count

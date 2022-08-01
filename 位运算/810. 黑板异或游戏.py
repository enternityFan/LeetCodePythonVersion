# @Time : 2022-08-01 20:36
# @Author : Phalange
# @File : 810. 黑板异或游戏.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def xorGame(self, nums: List[int]) -> bool:
        if len(nums) %2 == 0:
            return True
        tmp = 0
        for i in range(len(nums)):
            tmp ^=nums[i]
        if tmp == 0:
            return True

        return False


print(Solution().xorGame([1,0,0,0,1,0,0,0,1,0,1]))
print(Solution().xorGame([1,1,2]))
print(Solution().xorGame([0,1]))
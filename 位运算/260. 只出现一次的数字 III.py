# @Time : 2022-08-04 19:11
# @Author : Phalange
# @File : 260. 只出现一次的数字 III.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            return nums
        n = 0
        for x in nums:
            n ^=x

        rightOne = n & (~n+1) # 得到n最右边的值
        # 这两个数的rightOne位，一个是1，一个是0说明
        num1 = 0
        num2 = 0
        for x in nums:
            if x & rightOne == rightOne: #这一位位1
                num1 ^=x
            else:
                num2 ^=x
        return [num1,num2]

print(Solution().singleNumber([1,2,1,3,2,5]))
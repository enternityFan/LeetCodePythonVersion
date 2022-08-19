# @Time : 2022-08-19 10:46
# @Author : Phalange
# @File : 1909. 删除一个元素使数组严格递增.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:

        flag = False
        n = len(nums)
        for i in range(n):
            tmp = False
            for j in range(n):
                if j == i:
                    continue

                if j!=0:
                    if j == i+1:
                        if j -2 >=0 and nums[j] <= nums[j-2]:
                            tmp = True
                            break
                    elif nums[j] <=nums[j-1]:
                        tmp = True
                        break
            if tmp == False:
                return True


        return flag

print(Solution().canBeIncreasing([100,21,100]))
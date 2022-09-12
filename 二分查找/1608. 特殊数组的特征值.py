# @Time : 2022-08-01 22:10
# @Author : Phalange
# @File : 1608. 特殊数组的特征值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        [1,2,2,3,5]

        :param nums:
        :return:
        """
        nums = sorted(nums)

        res = -1
        length = len(nums)

        l = 1
        r = length
        while l<=r:
            mid = l + ((r-l) >> 1)
            cnt = 0
            for each in nums:
                if each >=mid:
                    cnt +=1

            if cnt ==mid:
                res = mid
                break
            elif cnt < mid:
                r = mid - 1
            else:
                l = mid + 1
        return res



print(Solution().specialArray([3,5]))
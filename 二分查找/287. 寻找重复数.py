# @Time : 2022-08-01 21:43
# @Author : Phalange
# @File : 287. 寻找重复数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        二分算法求解
        因为数字都是在[1,n]这个范围内的，假设[1,2,2,3,4,5]
        mid = 1 + (5 - 1) / 2 = 3, 把小于3的数目算一下为4，说明【1，3】之间一定有重复值

        :param nums:
        :return:
        """

        l = 1
        r = len(nums)-1
        ans = -1
        while l <= r:
            mid = l + ((r - l) >>1)
            cnt = 0
            for i in range(len(nums)):
                if nums[i] <= mid:
                    cnt +=1
            if cnt <= mid:
                l = mid+1
                ans = mid
            else:
                r = mid - 1

        return ans

print(Solution().findDuplicate([1,3,4,2,2]))
print(Solution().findDuplicate([3,1,3,4,2]))
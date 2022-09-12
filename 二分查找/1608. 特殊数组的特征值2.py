# @Time : 2022-09-12 14:13
# @Author : Phalange
# @File : 1608. 特殊数组的特征值2.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    """
    [1,2,2,3,4,5]
    """
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        ans = -1
        for i in range(len(nums)+1):
            l = 0
            r = len(nums)-1

            while l <= r:
                mid = l + ((r - l) >> 1)
                #print(mid)
                # if nums[mid] == i:
                #     if len(nums) - mid == i:
                #         ans = i
                #     break

                if nums[mid] >=i:
                    if len(nums) - mid == i and ((mid-1>0 and nums[mid-1] < i) or mid == 0):
                        ans = i
                        break


                    r = mid - 1
                else:
                    l = mid + 1


        return ans

print(Solution().specialArray([1,2,2,3,4,5]))
print(Solution().specialArray([3,5]))
print(Solution().specialArray([3,9,7,8,3,8,6,6]))
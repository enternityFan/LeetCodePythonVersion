# @Time : 2022-07-29 16:44
# @Author : Phalange
# @File : 350. 两个数组的交集 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        p1 = 0
        p2 = 0
        res = []
        while p1 <len(nums1) and p2 <len(nums2):
            if nums1[p1] > nums2[p2]:
                p2 +=1
            elif nums1[p1] < nums2[p2]:
                p1 +=1
            else:
                res.append(nums1[p1])
                p1 +=1
                p2 +=1
        return res


s = Solution()
a1 = [4,9,5]
a2 = [9,4,9,8,4]
print(s.intersect(a1,a2))
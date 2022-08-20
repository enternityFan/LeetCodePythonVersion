# @Time : 2022-08-20 20:47
# @Author : Phalange
# @File : 496. 下一个更大元素 I.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = collections.defaultdict(int)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]] < nums2[i]:
                idx = stack.pop()
                ans[nums2[idx]] = nums2[i]
            stack.append(i)

        ans2 = []
        for i in range(len(nums1)):
            if nums1[i] not in ans:
                ans2.append(-1)
            else:
                ans2.append(ans[nums1[i]])

        return ans2

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(Solution().nextGreaterElement(nums1,nums2))
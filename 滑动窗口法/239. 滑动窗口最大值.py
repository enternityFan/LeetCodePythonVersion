# @Time : 2022-08-20 15:09
# @Author : Phalange
# @File : 239. 滑动窗口最大值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        n = len(nums)
        ans = [0] * (n-k+1)
        idx = 0
        qmax = collections.deque()
        for R in range(n):
            while len(qmax)!=0 and nums[qmax[-1]] <= nums[R]:

                qmax.pop()
            qmax.append(R)

            if qmax[0] == R-k:
                qmax.popleft()

            if (R >=k-1):
                ans[idx] = nums[qmax[0]]
                idx +=1
        return ans

print(Solution().maxSlidingWindow([12,3,4,5,2],2))
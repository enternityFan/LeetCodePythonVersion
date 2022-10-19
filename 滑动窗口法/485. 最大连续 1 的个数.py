# @Time : 2022-08-20 16:57
# @Author : Phalange
# @File : 485. 最大连续 1 的个数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        ans = 0
        mywindows = collections.deque()
        for i in range(n):
            if nums[i] == 1:
                mywindows.append(nums[i])
            else:
                ans = max(ans,len(mywindows))
                mywindows.clear()

        return max(ans,len(mywindows))


class Solution2:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxVal = -1
        n = len(nums)
        if n == 1:
            return nums[0]
        st = -1
        ed = -1
        for i in range(n):
            if nums[i] == 0 and st !=-1:
                maxVal = max(maxVal,ed-st+1)
                st = -1
                ed = -1
            elif nums[i] == 1:
                if st == -1:
                    st = i
                    ed = i
                else:
                    ed +=1
        if maxVal == -1 and st == -1 and ed == -1:
            return 0
        maxVal = max(maxVal,ed-st+1)
        return maxVal

print(Solution().findMaxConsecutiveOnes([0,0]))
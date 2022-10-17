# @Time : 2022-10-17 12:13
# @Author : Phalange
# @File : 1004. 最大连续1的个数 III.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mywin = collections.deque()
        ans = 0
        num_zero = 0
        for i in range(len(nums)):
            if num_zero <k and nums[i] == 0:
                mywin.append(nums[i])
                num_zero +=1
            elif nums[i] == 1:
                mywin.append(nums[i])
            elif num_zero == k:
                if k !=0:
                    ans = max(ans,len(mywin))
                    while num_zero ==k:
                        tmp = mywin.popleft()
                        if tmp == 0:
                            num_zero -=1
                    mywin.append(nums[i])
                    num_zero +=1
                else:
                    ans = max(ans,len(mywin))
                    mywin.clear()

        if num_zero !=0 or k == 0:
            ans = max(ans,len(mywin))

        return ans

nums = [0,0,1,1,1,0,0]
K = 0
print(Solution().longestOnes(nums,K))



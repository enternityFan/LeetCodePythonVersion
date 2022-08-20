# @Time : 2022-08-20 20:59
# @Author : Phalange
# @File : 503. 下一个更大元素 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n
        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                ans[idx] = nums[i]
            stack.append(i)

        idx = stack[-1] # 这个是最后的索引，就是到这里，正好走一个圈。
        # 这个时候是stack中剩下的，那么我要去他之前的位置进行寻找有没有比他大的
        i= idx
        while i !=idx-1:
            if i >=n:
                idx +=2
                i=0
            while stack and nums[stack[-1]] < nums[i]:
                prev_idx = stack.pop()
                ans[prev_idx] = nums[i]

            i +=1


        return ans

nums = [1,2,1]
print(Solution().nextGreaterElements(nums))
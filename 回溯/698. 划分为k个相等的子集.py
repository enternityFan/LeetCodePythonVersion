# @Time : 2022-09-20 14:09
# @Author : Phalange
# @File : 698. 划分为k个相等的子集.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:

    def __init__(self):
        self.ans = []
        self.tmp = []
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        def process(nums,idx,val,target,used):
            if val == target:
                if self.tmp not in self.ans:
                    self.ans.append(self.tmp[:])
                return
            if idx == len(nums) or val > target:
                return
            process(nums,idx+1,val,target,used)
            if idx not in used:
                self.tmp.append(nums[idx])
                used.add(idx)
                process(nums,idx+1,val+nums[idx],target,used)
                print(used)
                used.remove(idx)
                self.tmp.pop()



        if sum(nums) % k !=0:
            return False
        target = sum((nums)) // k
        nums.sort()
        used = set()
        process(nums,0,0,target,used)
        #return len(self.ans) == k
        return self.ans

nums = [4,3,2,3,5,2,1]
nums = [1,1,1,1,2,2,2,2]
print(Solution().canPartitionKSubsets(nums,2))


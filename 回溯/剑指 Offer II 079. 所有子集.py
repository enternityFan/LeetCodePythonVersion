# @Time : 2022-08-10 18:24
# @Author : Phalange
# @File : 剑指 Offer II 079. 所有子集.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = []
        self.tmp = []
        self.set = set()

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.f(nums,0,[])
        return self.ans


    def f(self,nums,index,path):
        if index == len(nums):
            self.ans.append(path[:])
            return
        tmpset = [0]*10
        if tmpset[index] == 0:
            tmpset[index] = 1

            self.f(nums,index+1,path)
            path.append(nums[index])
            self.f(nums,index+1,path)
            path.pop()
print(Solution().subsets([1,2,3]))

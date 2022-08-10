# @Time : 2022-08-10 20:25
# @Author : Phalange
# @File : 1863. 找出所有子集的异或总和再求和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def __init__(self):
        self.ans = [] #存放所有子集
    def subsetXORSum(self, nums: List[int]) -> int:

        self.f(nums,0,[])
        result = 0
        for each in self.ans:
            if each == []:
                continue
            tmp = 0
            for x in each:
                tmp ^=x
            result +=tmp
        return result


    def f(self,nums,idx,path):
        if idx == len(nums):
            self.ans.append(path[:])
            return
        self.f(nums,idx+1,path)
        path.append(nums[idx])
        self.f(nums,idx+1,path)
        path.pop()

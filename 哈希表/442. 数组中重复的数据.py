# @Time : 2022-07-29 16:52
# @Author : Phalange
# @File : 442. 数组中重复的数据.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        mydict = {}
        res = []
        for each in nums:
            if each in mydict:
                res.append(each)
            else:
                mydict[each] = 1
        return res

a = [4,3,2,7,8,2,3,1]
s = Solution()
print(s.findDuplicates(a))
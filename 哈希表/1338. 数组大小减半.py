# @Time : 2022-08-01 11:26
# @Author : Phalange
# @File : 1338. 数组大小减半.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
import heapq
from typing import List

# 解法1  用哈希表
class Solution1:
    def minSetSize(self, arr: List[int]) -> int:

        mydict = collections.defaultdict(int)
        for i in range(len(arr)):
            mydict[arr[i]] +=1
        mydict = sorted(mydict.items(),key=lambda x:x[1],reverse=True)

        k = len(arr) //2
        tmp = 0
        idx =0
        for i,item in enumerate(mydict):
            tmp +=item[1]
            if tmp >= k:
                idx = i+1
                break
        return idx






print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))
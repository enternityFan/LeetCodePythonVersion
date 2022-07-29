# @Time : 2022-07-29 21:02
# @Author : Phalange
# @File : 剑指 Offer II 033. 变位词组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        arr = []
        for eachs in strs:
            mydict = collections.defaultdict(int)
            for c in eachs:
                mydict[c] +=1

            arr.append(mydict)

        res = []
        idx = [0] * len(strs) # 用来标记是否已经取过
        for i,each in enumerate(arr):
            tmp = []
            tmp.append(strs[i])
            if idx[i] == 1:
                continue

            idx[i] = 1
            for j in range(i+1,len(arr)):
                if arr[j] == arr[i]:
                    tmp.append(strs[j])
                    idx[j] = 1
            res.append(tmp)
        return res



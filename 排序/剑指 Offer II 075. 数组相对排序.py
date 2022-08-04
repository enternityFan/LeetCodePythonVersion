# @Time : 2022-08-04 13:32
# @Author : Phalange
# @File : 剑指 Offer II 075. 数组相对排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = max(arr1)
        cnt = [0] * (m + 1)

        for x in arr1:
            cnt[x] +=1

        ans = []
        for x in arr2:
            ans.extend([x] * cnt[x])
            cnt[x] = 0
        for i in range(m+1):
            if cnt[i] !=0:
                ans.extend([i] * cnt[i])
                cnt[i] = 0
        return ans
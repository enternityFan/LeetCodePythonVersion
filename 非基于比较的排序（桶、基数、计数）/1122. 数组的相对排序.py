# @Time : 2022-08-04 13:06
# @Author : Phalange
# @File : 1122. 数组的相对排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = max(arr1)
        cnt = [0] * (m+1)
        for i in range(len(arr1)):
            cnt[arr1[i]] +=1

        ans = []
        for x in arr2:
            ans.extend([x] * cnt[x])
            cnt[x] = 0
        for x in range(m+1):
            if cnt[x] >0:
                ans.extend([x] * cnt[x])

        return ans



arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(Solution().relativeSortArray(arr1,arr2))
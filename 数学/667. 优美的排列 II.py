# @Time : 2022-09-08 14:18
# @Author : Phalange
# @File : 667. 优美的排列 II.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = list(range(1,n-k))
        i,j = n - k,n
        while i <=j:
            ans.append(i)
            if i !=j:
                ans.append(j)

            i,j = i+1,j-1
        return ans



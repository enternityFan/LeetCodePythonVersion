# @Time : 2022-03-02 17:50
# @Author : Phalange
# @File : 剑指 Offer II 003. 前 n 个数字二进制中 1 的个数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import *

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0,1,1,2]
        if n <=3:
            return res[:n+1]
        for each in range(4,n+1,2):
            res.append(res[each//2])
            res.append(res[each//2]+1)
        if n %2 != 0 :
            return res
        else:
            return res[:-1]





S = Solution()
a = S.countBits(5)
print(a)
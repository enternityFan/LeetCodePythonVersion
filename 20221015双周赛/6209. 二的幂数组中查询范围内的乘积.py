# @Time : 2022-10-15 22:51
# @Author : Phalange
# @File : 6209. 二的幂数组中查询范围内的乘积.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        powers = []
        ans = []
        tmp  = 1
        while tmp <= n:
            tmp *=2
        tmp //=2
        n2 = n
        while n2 >0:
            if n2 - tmp >=0:
                n2 -=tmp
                powers.append(tmp)
            else:
                tmp >>=1
        powers.sort()
        for each in queries:
            tmp = 1
            for i in range(each[0],each[1]+1):
                tmp =(tmp * powers[i]) % (1000000000 + 7)
            ans.append(tmp)
        return ans

print(Solution().productQueries(2,[[0,0]]))
print(Solution().productQueries(15,[[0,1],[2,2],[0,3]]))

# @Time : 2022-09-18 12:51
# @Author : Phalange
# @File : 313. 超级丑数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        if n <=len(primes):
            return primes[n-1]
        lp = len(primes)
        dp = [[0]*1000 for _ in range(lp)]
        ans = [1]
        for i in range(lp):
            dp[lp][0] = primes[i]
        prevMin = [2]*lp
        for i in range(lp):
            for j in range(1,1000):
                dp[i][j] = dp[i][j-1]*prevMin[i]
                # 更新一下prevMin
                for k in range(1,lp):
                    pass





        return ans[-1]
# @Time : 2022-08-19 11:29
# @Author : Phalange
# @File : 441. 排列硬币.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D

import math

class Solution:
    def arrangeCoins(self, n: int) -> int:

        ans = 1
        tmp = ans
        while n > 0:
            if tmp == n:
                return ans
            elif tmp > n:
                ans = ans-1
                break

            ans +=1
            tmp +=ans
        return ans

print(Solution().arrangeCoins(8))
# @Time : 2022-08-11 21:59
# @Author : Phalange
# @File : 1925. 统计平方和三元组的数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            for j in range(1,n+1):
                c = int(math.sqrt(i**2 + j ** 2+1))
                print(c,i,j)
                if c <=n and c ** 2 == i ** 2 + j ** 2:

                    ans +=1

        return ans

print(Solution().countTriples(5))


# @Time : 2022-09-13 22:03
# @Author : Phalange
# @File : 397. 整数替换.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 2:
            return 1
        elif n == 3:
            return 2
        elif n % 2 == 0:
            return 1 + self.integerReplacement(n // 2)
        else:
            return 1 + min(self.integerReplacement(n+1),self.integerReplacement(n-1))



        # while n!=1:
        #     print(n)
        #     if n % 2 == 0:
        #         tmp = math.modf(math.log2(n))
        #         if not tmp[0]:
        #             ans += int(tmp[1])
        #             break
        #         ans +=1
        #         n = n //2
        #     else:
        #         if n == 3:
        #             ans +=2
        #             break
        #         tmp = math.modf(math.log2(n+1))
        #         if not tmp[0]:
        #             ans += int(tmp[1]) + 1
        #             break
        #         else:
        #             ans +=1
        #             n = n - 1

        return ans
print(Solution().integerReplacement(10000))
print(Solution().integerReplacement(7))
print(Solution().integerReplacement(15))
print(Solution().integerReplacement(16))
print(Solution().integerReplacement(1234))
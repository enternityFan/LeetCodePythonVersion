# @Time : 2022-10-14 8:19
# @Author : Phalange
# @File : 633. 平方数之和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        j = int(math.sqrt(c))
        i = 0
        while i <=j:
            total = i ** 2 + j ** 2
            if total > c:
                j -=1
            elif total < c:
                i +=1
            else:
                return True

        return False



class Solution2:
    def judgeSquareSum(self, c: int) -> bool:
        n = int(math.sqrt(c))
        for i in range(n+1):
            l = i
            r = n
            while l <=r:
                mid = l + ((r - l) >> 1)
                if mid ** 2 == c - i ** 2:
                    return True
                elif mid **2> c - i ** 2:
                    r = mid - 1
                else:
                    l = mid + 1
        return False

print(Solution().judgeSquareSum(2))
print(Solution().judgeSquareSum(3))
print(Solution().judgeSquareSum(5))
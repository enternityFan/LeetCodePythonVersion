# @Time : 2022-07-29 8:04
# @Author : Phalange
# @File : 50. Pow(x, n).py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # way 1
        #return x ** n

        # way 2  快速幂加递归
        def func(N):
            if N == 0:
                return 1.0
            y = func(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return func(n) if n >=0 else 1.0 / func(-n)




s = Solution()

print(s.myPow(2,10))
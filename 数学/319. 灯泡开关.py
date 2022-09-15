# @Time : 2022-09-15 12:20
# @Author : Phalange
# @File : 319. 灯泡开关.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import math


class Solution:
    def bulbSwitch(self, n: int) -> int:
        """

        8
        0 0 0 0 0 0 0 0 0
        1 1 1 1 1 1 1 1 1    8
        1 0 1 0 1 0 1 0 1    4
        1 0 0 0 1 1 1 0 0    4
        1 0 0 1 1 1 1 1 0    6
        1 0 0 1 0 1 1 1 0    5
        1 0 0 1 0 0 1 1 0    4
        1 0 0 1 0 0 0 1 0    3
        1 0 0 1 0 0 0 0 0    2
        1 0 0 1 0 0 0 0 1
        n is even.
        第一轮切换n个状态
        第二轮切换n/2个状态
        第三轮切换n/3个状态
        。。
        。
        第n轮切换1个状态
        本来是全0的
        1 1 1 1
        1 0 1 0
        1 0 0 0
        1 0 0 1
        一共切换了(n - n/2 + n/3 + n/4 + n/5 + n/6... + 1)次状态；
        一共切换了(n/n + 2/3n +


        """
        if n == 0:
            return 0
        ans = 0
        i = 1
        while i <=n:
            if i * i <=n:
                ans +=1
            else:
                break
            i+=1


        return ans

print(Solution().bulbSwitch(3))
print(Solution().bulbSwitch(1))
print(Solution().bulbSwitch(4))
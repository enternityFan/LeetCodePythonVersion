# @Time : 2022-09-18 11:51
# @Author : Phalange
# @File : 2335. 装满杯子需要的最短总时长.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        n = len(amount)
        while amount[0] >0 or amount[1] > 0 or amount[2] > 0:
            amount.sort()
            if amount[1] > 0 and amount[2] > 0:
                amount[1] -=1
                amount[2] -=1
            else:
                amount[2] -=1

            ans +=1




        return ans
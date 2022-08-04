# @Time : 2022-08-04 18:50
# @Author : Phalange
# @File : 1672. 最富有客户的资产总量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxV = -1000
        for i in range(len(accounts)):
            maxV = max(maxV,sum(accounts[i]))

        return maxV

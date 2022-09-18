# @Time : 2022-09-18 12:17
# @Author : Phalange
# @File : 2279. 装满石头的背包的最大数量.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        needs = []
        n = len(capacity)
        for i in range(n):
            needs.append(capacity[i]-rocks[i])
        ans = 0
        if sum(needs) <= additionalRocks:
            return n
        needs.sort()
        i = 0
        while additionalRocks:
            if needs[i] == 0:
                ans +=1
            else:
                additionalRocks -=needs[i]
                if additionalRocks >=0:
                    ans +=1
                else:
                    break

            i +=1


        return ans

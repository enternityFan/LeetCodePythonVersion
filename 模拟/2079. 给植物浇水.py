# @Time : 2022-10-14 9:07
# @Author : Phalange
# @File : 2079. 给植物浇水.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        ans = 0
        curWater = capacity
        for i in range(len(plants)):
            if curWater - plants[i] <0:
                ans +=2*i
                curWater = capacity
            if curWater - plants[i] >=0:
                curWater -=plants[i]
                ans +=1
        return ans

print(Solution().wateringPlants([2,2,3,3],5))
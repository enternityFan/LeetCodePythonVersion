# @Time : 2022-09-08 21:08
# @Author : Phalange
# @File : 2391. 收集垃圾的最少总时间.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        car = [0,0,0,0,0,0] # 前三个记录耗时，后三个位置记录的是上一次车在哪收的
        for i,each in enumerate(garbage):
            if "M" in each:
                car[0] += each.count("M")

                if i !=0:
                    car[0] +=sum(travel[car[3]:i])
                    car[3] = i
            if "P" in each:
                car[1] += each.count("P")

                if i !=0:
                    car[1] +=sum(travel[car[4]:i])
                    car[4] = i
            if "G" in each:
                car[2] += each.count("G")

                if i !=0:
                    car[2] +=sum(travel[car[5]:i])
                    car[5] = i
        return sum(car[:3])

garbage = ["G","P","GP","GG"]
travel = [2,4,3]
print(Solution().garbageCollection(garbage,travel))

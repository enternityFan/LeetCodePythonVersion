# @Time : 2022-07-30 19:09
# @Author : Phalange
# @File : 973. 最接近原点的 K 个点.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """

        如果我在计算距离的时候，省去一步开方的操作，然后我上传了5次答案，平均耗时181ms
        如果不省去开放操作，上传5次平均耗时184，没啥区别。。
        :param points:
        :param k:
        :return:
        """
        distance = [(point[0] ** 2 + point[1] ** 2) ** 0.5 for point in points]
        #distance = [point[0]**2 + point[1]**2 for point in points]
        distance,points = (list(t) for t in zip(*sorted(zip(distance,points),key=lambda x:x[0])))
        return points[:k]


class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:k]

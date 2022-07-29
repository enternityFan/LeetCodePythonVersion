# @Time : 2022-07-29 14:10
# @Author : Phalange
# @File : 223. 矩形面积.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:



        S1 = (ax2 - ax1) * (ay2 - ay1)
        S2 = (bx2 - bx1) * (by2 - by1)
        # 然后根据题解。。。减去一个重叠的面积就行了。
        overW = min(ax2,bx2) - max(ax1,bx1)
        overH = min(ay2,by2) - max(ay1,by1)
        oA = max(overW,0) * max(overH,0)
        return S1 + S2 - oA







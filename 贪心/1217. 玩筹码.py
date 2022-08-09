# @Time : 2022-08-09 17:51
# @Author : Phalange
# @File : 1217. 玩筹码.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        """
        奇变偶，或者偶变奇，这个时候会消耗代价
        而奇不变偶，或者偶不变奇，这个时候不消耗代价
        :param position:
        :return:
        """
        count = [0,0]#统计多少个奇数，多少个偶数
        for each in position:
            if each % 2 == 0:
                count[0] +=1
            else:
                count[1] +=1
        return min(count)
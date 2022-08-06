# @Time : 2022-08-05 18:29
# @Author : Phalange
# @File : 1561. 你可以获得的最大硬币数目.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles)
        n = len(piles) //3 # 要分n堆
        ans = 0
        pt1 = 0
        pt2 = len(piles) -2 # 第二大的堆
        while pt1 <= pt2:
            ans +=piles[pt2]
            #print(piles[pt2])

            pt1 +=1
            pt2 -=2
        return ans

print(Solution().maxCoins([2,4,1,2,7,8]))
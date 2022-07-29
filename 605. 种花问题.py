# @Time : 2022-07-29 9:28
# @Author : Phalange
# @File : 605. 种花问题.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        假设花坛的长度是m，当m是奇数的时候，最多可以种m//2 + 1个花，是偶数的时候最多是m//2的花
        对于三个花洞，正常来说是和为1的，对于和为0的情况，可以再种一个，种的位置就是中间的位置
        """
        m = len(flowerbed)
        res = 0
        for i in range(m):
            # 判断这个位置可以种花不可以
            if flowerbed[i] == 0 and (i + 1 == m or flowerbed[i+1] == 0) and (i==0 or flowerbed[i-1] == 0):
                res +=1
                flowerbed[i] = 1

        return res >=n









s = Solution()

print(s.canPlaceFlowers([1,0,0,0,1],2))
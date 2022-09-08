# @Time : 2022-09-08 20:49
# @Author : Phalange
# @File : 888. 公平的糖果交换.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List

# TODO这个题应该用二分做。
class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSizes.sort()
        bobSizes.sort()
        sum1 = sum(aliceSizes)
        sum2 = sum(bobSizes)
        for i in range(len(bobSizes)):
            l = 0
            r = len(aliceSizes)-1
            while l <=r:
                mid = l + ((r - l) >> 1)
                tmp1 = sum1 - aliceSizes[mid] + bobSizes[i]
                tmp2 = sum2 - bobSizes[i] + aliceSizes[mid]
                if tmp1 == tmp2:
                    return [aliceSizes[mid],bobSizes[i]]
                elif tmp1 > tmp2:
                    r = mid - 1
                else:
                    r = mid + 1


aliceSizes = [1,2]
bobSizes = [2,3]
print(Solution().fairCandySwap(aliceSizes,bobSizes))
# @Time : 2022-08-20 12:10
# @Author : Phalange
# @File : 1356. 根据数字二进制下 1 的数目排序.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        return sorted(arr, key=lambda x: (bin(x).count("1"), x))


print(Solution().sortByBits([1024,512,256,128,64,32,16,8,4,2,1]))


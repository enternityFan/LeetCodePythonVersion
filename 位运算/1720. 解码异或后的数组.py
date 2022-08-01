# @Time : 2022-08-01 20:18
# @Author : Phalange
# @File : 1720. 解码异或后的数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        arr = [first]

        for i in range(len(encoded)):
            arr.append(encoded[i] ^ arr[i])


        return arr

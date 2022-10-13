# @Time : 2022-10-11 21:06
# @Author : Phalange
# @File : 2433. 找出前缀异或的原始数组.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [0]
        for i in range(len(pref)):
            if i == 0:
                arr[i] = pref[i]
                continue
            arr.append(pref[i] ^ pref[i-1])


        return arr
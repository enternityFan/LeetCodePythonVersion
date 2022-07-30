# @Time : 2022-07-30 18:34
# @Author : Phalange
# @File : 1588. 所有奇数长度子数组的和.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:

        res = 0
        windows = list(range(1,len(arr)+1,2))
        for w in windows:
            tmp = 0 # 记录这个窗口下面的全部的和
            for i in range(0,len(arr)):
                if i < w:
                    tmp += arr[i]
                else:
                    print(tmp)
                    res +=tmp # 首先把这个列表的值给加进去
                    tmp -=arr[i-w]#维护这个前缀吧
                    tmp +=arr[i]
            res +=tmp
            print(tmp)
        return res

s = Solution()
print(s.sumOddLengthSubarrays([1,4,2,5,3]))


# @Time : 2022-08-20 17:24
# @Author : Phalange
# @File : 2283. 判断一个数的数字计数是否等于数位的值.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def digitCount(self, num: str) -> bool:
        mymap = collections.Counter(num)
        for i in range(len(num)):

            if int(num[i]) != mymap[str(i)]:
                return False
        return True

print(Solution().digitCount("1210"))
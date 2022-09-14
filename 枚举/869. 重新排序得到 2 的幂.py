# @Time : 2022-09-14 21:20
# @Author : Phalange
# @File : 869. 重新排序得到 2 的幂.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        mydict = collections.defaultdict(list)
        ans = False
        val = 1
        while val <=1e9:
            strval = str(val)
            mydict[len(strval)].append(strval)
            val = val * 2

        strn = str(n)
        for each in mydict[len(strn)]:
            tmp1 = sorted(each)
            tmp2 = sorted(strn)
            if tmp2 == tmp1:
                return True

        return False

print(Solution().reorderedPowerOf2(10))


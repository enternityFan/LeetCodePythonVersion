# @Time : 2022-09-13 13:08
# @Author : Phalange
# @File : 670. 最大交换.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def maximumSwap(self, num: int) -> int:
        strnum = [c for c in str(num)]
        mydict = {}#存储每个数最后出现的位置
        for i in range(len(strnum)):
            mydict[strnum[i]] = i

        num2 = strnum.copy()
        num2.sort(reverse=True)


        j = 0
        for i in range(len(strnum)):
            if strnum[i] <num2[j]:
                strnum[i],strnum[mydict[num2[j]]] = strnum[mydict[num2[j]]],strnum[i]
                break
            j+=1
        return eval("".join(strnum))

print(Solution().maximumSwap(9973))
print(Solution().maximumSwap(1993))
print(Solution().maximumSwap(98368))

print(Solution().maximumSwap(99901))


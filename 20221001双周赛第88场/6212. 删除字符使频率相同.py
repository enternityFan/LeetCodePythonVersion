# @Time : 2022-10-01 22:30
# @Author : Phalange
# @File : 6212. 删除字符使频率相同.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def equalFrequency(self, word: str) -> bool:
        tmp = [0] * 26
        for c in word:
            tmp[ord(c) - ord('a')] +=1
        tmp.sort()
        flag = False
        cnt = 0

        for i in range(26):
            if tmp[i] !=0:
                tmp[i]-=1
                if len(set(tmp)) >2:
                    tmp[i] +=1
                    continue
                else:
                    flag = True



        return flag

print(Solution().equalFrequency("aazz"))
# @Time : 2022-07-30 17:43
# @Author : Phalange
# @File : 剑指 Offer II 015. 字符串中的所有变位词.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List
import collections

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        ls = len(s)
        lp = len(p)
        pdict = collections.defaultdict(int)
        for each in p:
            pdict[each] +=1

        if ls < lp:
            return []
        windows = s[0:lp] # 做一个滑动窗口加速
        flag = 0 # 用来记录当前的窗口是否满足条件
        i = lp - 1
        while i < ls:
            if flag == 1 and windows[0] == s[i]:
                # 更新一下窗口
                res.append(i-lp+1)
                windows = windows[1:] + s[i]
                i+=1
                continue
            elif flag == 1 and windows[0] !=s[i]:
                #不相同了，那我就直接跳到这个位置不就行了
                flag = 0
                if s[i] not in windows:

                    i +=lp
                else:
                    i +=1
            else:


                sdict = collections.defaultdict(int)
                for j in range(i-lp+1,i+1):
                    sdict[s[j]]+=1
                if sdict == pdict:
                    res.append(i-lp+1)
                    windows = s[i-lp+1:i+1]
                    flag = 1
                else:
                    flag = 0
                i +=1
        return res


s = Solution()
print(s.findAnagrams("abacbabc","abc"))
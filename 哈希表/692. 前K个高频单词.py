# @Time : 2022-07-27 17:39
# @Author : Phalange
# @File : 692. 前K个高频单词.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort(reverse=False)

        mydict = {}
        for each in words:
            if each in mydict:
                mydict[each] +=1
            else:
                mydict[each] = 1

        mydict = sorted(mydict.items(),key=lambda x:x[1],reverse=True)
        result = []
        for i,key in enumerate(mydict):
            if i < k:
                result.append(key[0])
            else:
                break
        return result




s = Solution()
words = ["i", "love", "leetcode", "i", "love", "coding"]
print(s.topKFrequent(words,2))
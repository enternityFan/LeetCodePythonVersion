# @Time : 2022-08-14 13:07
# @Author : Phalange
# @File : 面试题 08.08. 有重复字符串的排列组合.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []
        tmp = [i for i in S]
        mydict = collections.Counter(S)
        def process(idx):
            if idx == len(S):
                mystr = "".join(tmp)
                if mystr not in ans:

                    ans.append(mystr)
                return

            chars = [0] * 52
            for i in range(idx,len(S)):
                if S[i] >= 'a' and S[i] <= 'z':
                    if chars[ord(S[i]) - ord('a')] < mydict[S[i]]:
                        chars[ord(S[i]) - ord('a')] += 1

                        tmp[i],tmp[idx] = tmp[idx],tmp[i]
                        process(idx+1)
                        tmp[i],tmp[idx] = tmp[idx],tmp[i]
                else:
                    if chars[ord(S[i]) - ord('A')] < mydict[S[i]]:
                        chars[ord(S[i]) - ord('A')] += 1

                        tmp[i],tmp[idx] = tmp[idx],tmp[i]
                        process(idx+1)
                        tmp[i],tmp[idx] = tmp[idx],tmp[i]
                # tmp[i],tmp[idx] = tmp[idx],tmp[i]
                # process(idx+1)
                # tmp[i],tmp[idx] = tmp[idx],tmp[i]


        process(0)

        return ans
print(Solution().permutation("Jfj"))
print(Solution().permutation("OSS"))
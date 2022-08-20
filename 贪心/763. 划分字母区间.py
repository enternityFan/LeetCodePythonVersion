# @Time : 2022-08-20 9:41
# @Author : Phalange
# @File : 763. 划分字母区间.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mymap = collections.defaultdict(int)
        n = len(s)
        for i in range(n):
            mymap[s[i]] = i #永远更新为最后一位
        st = 0#起始位置
        ed = 0#结束位置
        ans = []

        for i in range(n):
            if mymap[s[i]] > ed:
                ed = mymap[s[i]]# 更新一下这个位置
            elif i == ed:
                ans.append(ed-st+1)
                st = ed+1
                ed = ed+1

        return ans

print(Solution().partitionLabels("vhaagbqkaq"))
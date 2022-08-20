# @Time : 2022-08-20 9:52
# @Author : Phalange
# @File : 56. 合并区间.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        mymap = collections.defaultdict(int)
        sts = []
        for each in intervals:
            if (each[0] in mymap and each[1] > mymap[each[0]]) or each[0] not in mymap:
                mymap[each[0]] = each[1]
            sts.append(each[0])
        sts.sort()
        st = -1
        ed = 0
        ans = []
        for i in sts:
            if st == -1:
                st = i
                ed = mymap[i]
            if i > ed:
                ans.append([st,ed])
                st =i
                ed =mymap[i]
            elif mymap[i] > ed:
                ed = mymap[i]

        ans.append([st, ed])

        return ans


intervals = [[2,3],[5,5],[2,2],[3,4],[3,4]]
print(Solution().merge(intervals))
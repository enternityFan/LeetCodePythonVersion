# @Time : 2022-08-20 17:15
# @Author : Phalange
# @File : 2103. 环和杆.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def countPoints(self, rings: str) -> int:
        mymap = collections.defaultdict(set)
        n = len(rings)
        for i in range(0,n,2):
            mymap[rings[i+1]].add(rings[i])
        ans = 0
        for key,val in mymap.items():
            if len(val) ==3:
                ans +=1
        return ans
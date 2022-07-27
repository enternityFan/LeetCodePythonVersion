# @Time : 2022-07-27 17:08
# @Author : Phalange
# @File : 506. 相对名次.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = list(enumerate(score))
        score.sort(key = lambda x: x[1], reverse = True)# 从大到小排列
        res = [0] * len(score)
        for i,each in enumerate(res):
            if i == 0:
                res[score[i][0]] = "Gold Medal"
            elif i == 1:
                res[score[i][0]] = "Silver Medal"
            elif i == 2:
                res[score[i][0]] = "Bronze Medal"
            else:
                res[score[i][0]] = str(i+1)
        return res


s = Solution()


score = [5,4,3,2,1]
res = s.findRelativeRanks(score)
print(res)
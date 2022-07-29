# @Time : 2022-07-29 9:06
# @Author : Phalange
# @File : 1337. 矩阵中战斗力最弱的 K 行.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:


        m = len(mat)
        n = len(mat[0])
        weaker = [] #记录每行的战斗力
        weaker_idx = [] # 记录每行的索引
        for i in range(m):
            l = 0
            r = n
            pos = -1
            while l<=r and l < n:
                mid = l + (r-l) // 2
                if mat[i][mid] == 0:
                    r = mid -1
                else:
                    pos = mid
                    l = mid + 1


            if pos == -1:
                # 这一排都没有战斗力
                weaker.append(0)
            else:
                weaker.append(pos+1)
            weaker_idx.append(i)

        # 进行排序操作
        weaker, weaker_idx = (list(x) for x in zip(*sorted(zip(weaker, weaker_idx), key=lambda pair: pair[0])))
        return weaker_idx[:k]









mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3

s = Solution()
print(s.kWeakestRows(mat,3))
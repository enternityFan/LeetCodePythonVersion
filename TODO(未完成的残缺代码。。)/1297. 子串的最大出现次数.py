# @Time : 2022-10-17 12:58
# @Author : Phalange
# @File : 1297. 子串的最大出现次数.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n = len(s)
        ans = [0] * 26
        windows = {}
        cur_windows = [""] * (minSize - minSize+1)
        for i in range(minSize,maxSize+1):
            windows[i] = {}

        for i in range(n):

            for k in range(minSize,maxSize+1):
                if len(cur_windows[k-minSize]) <k:
                    cur_windows[k-minSize] +=s[i]
                else:
                    if cur_windows[k-minSize] not in windows[k]:
                        windows[k][cur_windows[k-minSize]] = 0
                    windows[k][cur_windows[k-minSize]] +=1
                    ans[k] = max(ans[k],windows[k][cur_windows[k-minSize]])


                    cur_windows[k-minSize] = cur_windows[k-minSize][1:] + s[i]


        return max(ans)

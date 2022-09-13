# @Time : 2022-09-13 13:41
# @Author : Phalange
# @File : 2038. 如果相邻两个颜色均相同则删除当前颜色.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        ans = True
        tmp = ""
        #AAAAABB
        mydict = {"AAA":0,"BBB":0}
        for i in range(len(colors)):
            if tmp =="" or colors[i] == tmp[-1]:
                tmp +=colors[i]
            else:
                tmp = colors[i]
            if len(tmp) ==3:
                mydict[tmp] +=1
                tmp = tmp[:-1]


        return mydict["AAA"] > mydict["BBB"]


print(Solution().winnerOfGame("AAAABBBB"))
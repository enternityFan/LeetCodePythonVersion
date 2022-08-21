# @Time : 2022-08-21 10:49
# @Author : Phalange
# @File : 6166. 最大回文数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D
import collections


class Solution:
    def largestPalindromic(self, num: str) -> str:
        if len(num) == 1:
            return num
        mydict = collections.Counter(num)
        ans = ""
        midNum = "" # 单独的一个数字
        sel = []
        for key,val in mydict.items():
            if val % 2 == 1:
                #谁长谁在中间，一样长的话比较大小
                if midNum !="":
                    if midNum < key:
                        midNum = key

                else:
                    midNum = key
                if val!=1:
                    mydict[key]-=1
                    sel.append(key)

            else:
                sel.append(key)

        if len(sel)>=1:
            sel.sort(key=lambda x: int(x))
            for i in range(len(sel)-1):
                ans = sel[i] * (mydict[sel[i]]//2) + ans + sel[i] * (mydict[sel[i]]//2)
            if sel[-1]!="0":
                ans = sel[-1] * (mydict[sel[-1]] // 2) + ans + sel[-1] * (mydict[sel[-1]] // 2)


        if midNum !="":
            ans = ans[:len(ans)//2] + midNum + ans[len(ans)//2:]

        return ans





print(Solution().largestPalindromic("44555"))
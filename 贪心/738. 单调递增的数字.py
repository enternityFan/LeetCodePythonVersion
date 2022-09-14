

"""
当且仅当每个相邻位数上的数字x和y满足x <= y时，我们称这个整数是单调递增的。

给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。
eg:10->9
eg:1234->1234
eg:1320->1299
eg:1329->1299
eg:21->19
eg:332->299
"""


class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        if n <10:
            return n
        arrn = [c for c in str(n)]
        flag = 0
        for i in range(1,len(arrn)):
            if flag:
                arrn[i] = '9'


            elif arrn[i-1] > arrn[i]:
                # 这一位不满足条件
                arrn[i-1] = chr(ord(arrn[i-1])-1)
                if i-2>=0:
                    for j in range(i-2,-1,-1):
                        if arrn[j] > arrn[j+1]:
                            arrn[j] = arrn[j+1]
                            arrn[j+1] = '9'



                arrn[i] = '9'
                flag = 1

        return eval("".join(arrn).lstrip('0'))

print(Solution().monotoneIncreasingDigits(1234))
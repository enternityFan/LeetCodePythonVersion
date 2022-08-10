# @Time : 2022-08-10 16:41
# @Author : Phalange
# @File : 640. 求解方程.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def solveEquation(self, equation: str) -> str:
        """
        ax + c = 0
        a = c = 0,无穷解
        a = 0,c!=0,无解
        其他情况都有解
        :param equation:
        :return:
        """
        a = 0
        c = 0
        flag = 1 # 控制正负号，1为正，-1为负
        flagequ = 1 # 表示当前在等号左边，-1表示在等号右边
        n = len(equation)
        temp = "0123456789"
        i = 0
        while i <n:
            if equation[i] in temp:
                #当前位是数字，那么我需要知道是否读完数字了
                val = int(equation[i])
                j = i+1
                while j<n and equation[j] in temp:
                    val = val * 10 + int(equation[j])
                    j +=1
                if j < n and equation[j] == 'x':
                    a += (val*flag)
                    i = j + 1
                else:
                    c +=(val*flag)
                    i = j

                continue
            elif equation[i] == 'x':
                a +=flag
            elif equation[i] == '-':
                flag = -1 * flagequ
            elif equation[i] == '+':
                flag = 1 * flagequ
            elif equation[i] == '=':
                flagequ = -1

                flag = flagequ

            i +=1
        if a == c and c == 0:
            return "Infinite solutions"
        elif a == 0 and c !=0:
            return "No solution"

        return "x=" + str(int(-c/a))

print(Solution().solveEquation("2x+3x-6x=x+2"))

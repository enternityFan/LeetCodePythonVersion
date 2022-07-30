# @Time : 2022-07-29 16:05
# @Author : Phalange
# @File : 12. 整数转罗马数字.py
# @Software: PyCharm
# C'est la vie,enjoy it! :D



class Solution:
    def intToRoman(self, num: int) -> str:
        mydict ={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M',4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        code = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        code = code[::-1]
        roman = ""
        # 1994
        idx = 1 # 记录位数
        while num >0:
            v = num % (10**idx)
            num -=v
            if v in mydict:
                roman =mydict[v] + roman# 因为最后输出的时候要逆序
            else:
                tmp = ""
                tmpidx = 0  # 加速循环吧相当于
                while v >0:

                    for i in range(tmpidx,len(code)):
                        if v - code[i] >=0:
                            tmp +=mydict[code[i]]
                            v -=code[i]
                            tmpidx = i
                            break
                roman = tmp + roman

            idx +=1




        return roman


s = Solution()
print(s.intToRoman(58))



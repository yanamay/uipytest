#升序输出出现频次最高的前三位[1,21,2,5,6,8,9,32,23,78,90,3,5,1,21,9,2,5,1,23]
a=[1,21,2,5,6,8,9,32,23,78,90,3,5,1,21,9,2,5,1,23]
listkey=[]
listvalue=[]
dict = {}
ll = 0
for i in set(a):
    listkey.append(i)
    listvalue.append(a.count(i))
    length=len(listvalue)
    while ll<length:
        dit={listvalue[ll]:listkey[ll]}
        dict.update(dit)
        ll+=1
    items=dict.items()
    backitems=[[v[0],v[1]] for v in items]
    backitems.sort(reverse=True)

print(backitems[:3])


'''
from unittest import mock
from unittest.mock import patch
import unittest
from test_dir import aacount

class Mockdemo(unittest.TestCase):
    @patch("aacount.multiply")
    #patch()装饰/上下文管理器可以很容易地模拟类或对象在模块测试。
    # 在测试过程中，您指定的对象将被替换为一个模拟（或其他对象），
    # 并在测试结束时还原。
    def test_add_and_multiply(self,mock_multiply):
        x=3
        y=5
        mock_multiply.return_value=15
        addition,multiple=aacount.add_and_multiply(x,y)
        mock_multiply.assert_called_once_with(3,5)
        self.assertEqual(8,addition)
        self.assertEqual(15,multiple)

if __name__=='__main__':
    unittest.main()
'''

'''
 def test_add(self):
        count1=aacount.count()
        #side_effect参数和return_value是相反的。它给mock分配了可替换的结果，覆盖了return_value。
        #简单的说，一个模拟工厂调用将返回side_effect值，而不是return_value。
        count1.add=mock.Mock(return_value=13,side_effect=count1.add)
        result=count1.add(8,8)
        print(result)
        count1.add.assert_called_with(8,8)#检查mock方法是否获得了正确的参数
        self.assertEqual(result,16)
        '''

'''
from selenium import webdriver
import  time
dr=webdriver.Chrome()
dr.get("http://www.smips.cn/")

#登录
dr.find_element_by_css_selector('div > div.text-input.el-input > input').send_keys('tengxun_admin')
dr.find_element_by_css_selector('form > div:nth-child(3) > div > div.el-input > input').send_keys('tengxun321')
dr.implicitly_wait(10)
dr.find_element_by_xpath('//*[@id="app"]/div/section[2]/form/div[4]/div/button').click()
dr.implicitly_wait(10)
dr.find_element_by_css_selector('#app > div > section.form_contianer > form > div:nth-child(5) > div > button').click()
time.sleep(2)
dr.get("http://www.smips.cn/manage/usertheme")
time.sleep(2)
dr.find_element_by_css_selector('.add_body>button').click()
time.sleep(2)
dr.find_element_by_css_selector('.add_body>div>input').send_keys('aaaa')
time.sleep(3)
'''

'''
import re
def is_mail_style(x):
    a=re.match(r'^[0-9a-zA-Z\_\-]*@[0-9a-zA-Z]+(\.com)$',x)
    if a:
        yhm=re.findall('^(.+?)@',x)
        print("yhm：%s" %yhm[0])
        gsm=re.findall('@(.+?)\.com',x)
        print("gsm:%s"%gsm[0])
        return True
    else:
        print("incorrect  email  format")
        return False
a=input("please enter emial:")
while 1:
    if a=='q' or a=='Q':
        exit()
    else:
        if is_mail_style(a):
            break
    a=input("please enter emial:")
print("下一步")
#如何遍历查找出某个文件夹内所有的子文件呢？并且找出某个后缀的所有文件
import os

def  get_files(path='F:\sss',rule='.py'):
    all=[]
    for fpathe,dirs,fs in os.walk(path):
        for f in fs:
            filename=os.path.join(fpathe,f)
            if filename.endswith(rule):
                all.append(filename)
    return all
if __name__=="__main__":
    b= get_files('F:\python\pyautoTest')
    for i in b:
        print(i)
'''
'''
#计算 n!,例如 n=3(计算 321=6)， 求 10!
from functools import  reduce
a=10
b=reduce(lambda x,y:x*y,range(1,a+1))
print(b)
#已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都
#等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据
a=0
b=1
while b<100:
    print(b,end=",")
    a,b=b,a+b
print(a)
#计算 x 的 n 次方，如：3 的 4 次方 为 3*3*3*3=81
def mi(x,n):
    if n==0:
        return 1
    else:
        return x*mi(x,n-1)
x=3
num=4
print(mi(x,num))
'''

'''
9.排序
用 python 写个冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
for i in range(len(a)):
    for j in range(len(a)-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
10.sort 排序,已知一个队列[1, 3, 6, 9, 7, 3, 4, 6],从小到大排序,按从大大小排序,去除重复数字
a = [1, 3, 6, 9, 7, 3, 4, 6]
# 1.sort 排序，正序a.sort()
print(a)
# 2.sort 倒 叙a.sort(reverse=True) print(a)
# 3.去重
b = list(set(a)) print(b)

'''

'''
7.水仙花打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身
。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋
5 的三次方＋3 的三次方。
sxh = []
for i in range(100, 1000):     
    s = 0
    m = list(str(i))
    for j in m:
        s += int(j)**len(m)
        if i == s:
            print(i)
            sxh.append(i)
print("100-999 的水仙花数：%s" % sxh)
8.完全数
如果一个数恰好等于它的因子之和，则称该数为“完全数”，又称完美数或完备数。
 例如：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余
3 个数相加，
1+2+3=6。第二个完全数是 28，它有约数 1、2、4、7、14、28，除去它本身 28 外，其余 5 个数相加，1+2+4+7+14=28。
那么问题来了，求 1000 以内的完全数有哪些？
a = []
for i in range(1, 1000):
    s = 0
    for j in range(1, i):
        if i % j == 0 and  j <  i:
            s += j
    if s == i:
        print(i)
        a.append(i)
print("1000 以内完全数：%s" % a)
5.队列
已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：
[3, 5, 1, 7]
a = [1, 3, 5, 7]
# insert 插入数据
a.insert(3, a[0])
print(a[1:])
6.交换
已知 a = 9, b = 8,如何交换 a 和 b 的值，得到 a 的值为 8,b 的值为 9
方法 1
a  = 8
b  = 9
a, b = b, a
print(a)
print(b)
方法 2
a  = 8
b  = 9
# 用中间变量 c 
c = a
a = b
b = c
print(a)
print(b)
'''

'''
3.字符串切割已知一个字符串为“hello_world_yoyo”, 如何得到一个队列["hello","world","yoyo"]
a = "hello_world_yoyo"
b = a.split("_")
print(b)

4.格式化输出
已知一个数字为 1，如何输出“0001”
a = 1
print("%04d" % a)
'''

'''
2.字符串切片
字符串 "axbyczdj"，如果得到结果“abcd”
方法一
# 字符串切片
a = "axbyczdj" print(a[::2])
方法二
# 传统思维
a = "axbyczdj"
c = []
for i in range(len(a)):
 if i % 2 == 0:
c.append(a[i])
print("".join(c))
'''

'''
1、统计在一个队列中的数字，有多少个正数，多少个负数，如[1, 3, 5, 7, 0, -1,-9, -4, -5, 8]
#方法一：
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# 用列表生成式，生成新的列表
b = [i for i in a if i > 0]
print("大于 0 的个数：%s" % len(b))
c = [i for i in a if i < 0]
print("小于 0 的个数：%s" % len(c))
#方法二
a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# 用传统的判断思维，累加m = 0
n  = 0
m=0
for i in a:
    if i > 0:
        m += 1
    elif i < 0:
        n += 1
else:
    pass
print("大于 0 的个数：%s" % m)
print("小于 0 的个数：%s" % n)
'''

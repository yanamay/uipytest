from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import csv
import codecs
from itertools import islice  #忽略首行



# 读取 CSV 文件
'''
data = csv.reader(codecs.open('info.csv', 'r', 'utf_8_sig'))
users = []
# 循环输出每一行信息
for line in islice(data, 1, None):
    users.append(line)
print(users)
'''

#操作txt文件
'''openfile=open('user_info.txt','r')
lines=openfile.readlines()
openfile.close()
for line in lines:
    username = line.split(',')[0]
    password = line.split(',')[1]
    asert = line.split(',')[2]
    print(username,password,asert)
    '''

#dr=webdriver.Chrome()
#dr.get('http://www.baidu.com')


#多窗口切换、获取一组数据
'''
dr.find_element_by_id('kw').send_keys('selenium')
dr.find_element_by_id('su').click()
time.sleep(3)

rr=dr.find_elements_by_css_selector("div>div[class='result c-container ']>h3>a")
for r in rr:
    print(r.text.encode("gbk","ignore").decode("gbk"))
    '''

#隐式等待
'''
try:
    print(time.ctime())
    ele=dr.find_element_by_id('kw22').send_keys('selenium')
except NoSuchElementException as e:
    print(e)
finally:
    print(time.ctime())
'''

#显示等待
'''
ele=WebDriverWait(dr,5,0.5).until(
    EC.element_to_be_clickable((By.ID,'kw')))
ele.send_keys('selenium')

print(time.ctime())
for i in range(10):
    try:
        el=dr.find_element_by_id('kw22')
        if el.is_displayed():
            break
    except:
        pass
    time.sleep(1)
else:
    print("time out")
print(time.ctime())
'''

#鼠标悬停、下拉框、警告框
'''
above=dr.find_element_by_partial_link_text('设置')
ActionChains(dr).move_to_element(above).perform()

dr.find_element_by_link_text('搜索设置').click()
time.sleep(3)
dr.find_element_by_css_selector("input[id=SL_2]").click()
time.sleep(3)
sel=dr.find_element_by_id('nr')
Select(sel).select_by_index(1)
time.sleep(3)
dr.find_element_by_class_name('prefpanelgo').click()
time.sleep(3)
alert=dr.switch_to.alert
alert.accept()
'''










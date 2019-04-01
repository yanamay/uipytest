import unittest
from time import localtime,strftime
import yagmail
from HTMLTestRunner import HTMLTestRunner

#实现发邮件
def send_mail(report_file):
    yag = yagmail.SMTP(user="836096322@qq.com",
                       password="yatou25692",
                       host='smtp.qq.com')
    contents = ['测试结果，请查看附件']
    mail_title="UI自动化测试报告"
    send_user=["836096322@qq.com"] #收件人信息
    yag.send(send_user, mail_title, contents,report_file)
    print("send mail out")

if __name__=="__main__":
    dicover = unittest.defaultTestLoader.discover('test_*.py')

    now_time = strftime("%Y_%m_%d %H_%M_%S")
    report_file = './report/' + now_time + '_result.html'
    report_name = open(report_file, 'wb')

    runner = HTMLTestRunner(stream=report_file,
                            verbosity=2,
                            title="百度测试报告",
                            description="运行环境：win 10，Chrome")
    runner.run(dicover)
    report_name.close()
    send_mail(report_file) #用例执行完成后，发送邮件
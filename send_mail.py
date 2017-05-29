#coding=utf8
# wei.wang what hurts more,the pain of hard work or the pain of regret?
__author__ = 'v'
__date__ = '2017/5/20'
import yagmail
# import smtplib
# from email.mime.text import MIMEText
#
#
_user = "wang_v9527@126.com"
# _pwd  = "liqowazdxmgjbjed"  #qq 授权码
_pwd  = "ww313688893"
_to   = input("请输入收件箱的地址>>>")
# _to   = "wang.v@hotmail.com"
_host = "smtp.126.com"
_port = 25
_body = input("请输入你要发送的邮件内容>>>")
_subject = input("请输入邮件的主题>>>")
print("邮件发送中，请稍等......")


def sendEmail():
    try:
        yag = yagmail.SMTP(user=_user, password=_pwd, host=_host, port=_port)
        # body = "王维，你好！我正在使用126邮箱给你发送测试邮件！请勿回复.谢谢！"
        yag.send(to=_to, subject=_subject, contents=_body)
        print("发送成功！！！")
    except:
        print("发送失败！！！")

sendEmail()

# msg = MIMEText("Test")  # 邮件内容
# msg["Subject"] = "王维测试邮件" # 邮件主题
# msg["From"] = _user # 发件人
# msg["To"] = _to # 收件人
#
# try:
#     s = smtplib.SMTP_SSL("smtp.qq.com", 465)
#     s.login(_user, _pwd)
#     s.sendmail(_user, _to, msg.as_string())
#     s.quit()
#     print("Success!")
# except smtplib.SMTPException as e:
#     print("Falied,%s" % e)
#

# yag = yagmail.SMTP(user=_user, password=_pwd, host=_host, port='465')
# body = "王维，你好！这是一封测试邮件！请勿回复"

# yag.send(to=_to, subject='测试邮件')
# print("Success send mail")

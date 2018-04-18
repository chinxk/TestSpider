from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def sent_email(password, msg):
    from_addr = 'chinxk@hotmail.com'
    # 输入收件人地址:
    to_addr = '107214108@qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.office365.com'
    msg = MIMEText(msg, 'plain', 'utf-8')
    msg['From'] = _format_addr('企鹅的HOTMAIL邮箱 <%s>' % from_addr)
    msg['To'] = _format_addr('企鹅的QQ邮箱 <%s>' % to_addr)
    msg['Subject'] = Header('最低价格通知', 'utf-8').encode()

    server = smtplib.SMTP()
    server.connect(smtp_server, 587)  # SMTP协议默认端口是25
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

if __name__ == '__main__':
    pw = input("email password: = ")
    sent_email(pw, msg)

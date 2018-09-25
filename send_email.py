"""
  emailフォーマット

"""

from email.mime.text import MIMEText
import smtplib

message = MIMEText('Hello, world.')  # 本文
message['Subject'] = 'Hello'         # 件名
message['From'] = 'official@webapp2.com'  # 送信元
message['To'] = 'test.akaunto319@gmail.com'      # 送信先

sender = smtplib.SMTP_SSL('smtp.muumuu-mail.com')
sender.login('official@webapp2.com', 'asatai951156')
sender.sendmail('official@webapp2.com', 'test.akaunto319@gmail.com', message.as_string())
sender.quit()

# coding=utf-8

# try:
#     from keys.local_keys.smtp_account import smtp_username, smtp_password
# except:
#     from djangoautoconf.settings_templates.smtp_account_template import smtp_username, smtp_password
from djangoautoconf.local_key_manager import get_local_key, ConfigurableAttributeGetter

# getter = ConfigurableAttributeGetter("smtp_account")
smtp_username = get_local_key("smtp_account.smtp_username")
smtp_password = get_local_key("smtp_account.smtp_password")
smtp_server = get_local_key("smtp_account.smtp_server")
smtp_port = get_local_key("smtp_account.smtp_port")
smtp_use_tls = get_local_key("smtp_account.smtp_use_tls")


# 邮件配置
EMAIL_HOST = smtp_server  # 'smtp.gmail.com'  # SMTP地址
EMAIL_PORT = smtp_port  # 25  # SMTP端口
EMAIL_HOST_USER = smtp_username  # 'pythonsuper@gmail.com'  # 我自己的邮箱
EMAIL_HOST_PASSWORD = smtp_password  # '******'  # 我的邮箱密码
# EMAIL_SUBJECT_PREFIX = u'[CoorCar网]'  # 为邮件Subject-line前缀,默认是'[django]'
EMAIL_USE_TLS = smtp_use_tls  # 与SMTP服务器通信时，是否启动TLS链接(安全链接)。默认是false
# 管理员站点
# SERVER_EMAIL = 'xxx@163.com'
# #The email address that error messages come from, such as those sent to ADMINS and MANAGERS.

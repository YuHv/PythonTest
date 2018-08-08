import numpy

import App_and_Key_Service as testApp
import testUser as addUser
import Login_Token as loginToken
from faker import Faker

fake = Faker("zh_CN")
import string
import random
import SelectTime as selTime
import UserInfo as userInfo

"""随机生成电话号码和邮箱"""
phone = fake.phone_number()
email = fake.email()

"""随机生成8到16位的密码"""
# password = ''
# for i in range(numpy.random.randint(8, 16)):
#     password += random.choice(string.digits + string.ascii_letters)
#
password = "123456q"
sum = 10

phone = '17828019328'
# password = "123456q"

if __name__ == '__main__':
    # 注册用户
    # addUser.AddUser(phone, email, password)

    # 获取登录token
    username = phone
    # access_token = 'Bearer' + loginToken.get_access_token_nuerpwd("17828019325", password)
    # access_token = 'Bearer' + loginToken.get_access_token_phone("17828019325")
    access_token = 'Bearer' +'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSB0dGFzIiwiY29kZSI6MCwidXNlcl9uYW1lIjoiMTc4MjgwMTkzMjUkMyIsInNjb3BlIjpbInNlcnZlciJdLCJleHAiOjE1MzM3MDE3NzQsImF1dGhvcml0aWVzIjpbImZyb250dXNlciIsIlJPTEVfVVNFUiJdLCJqdGkiOiJhN2RjYjlmNC0yMzRmLTQwNWItOTcxMS1kMzM5YTZkMzE2NjAiLCJjbGllbnRfaWQiOiJwaWcifQ.rcVVhH5bw1CsJMQRidNjNsIHVxZdNTmRB-dc-6kYX-A'
    # 获取当前用户信息
    userInfo.userInfo(access_token)

    # 对APP、AppKey操作
    testApp.app_And_key(sum, access_token)
    '''#
    # for i in range(1):
    #     radAppId = numpy.random.randint(1, sum)
    #     appkey = selKey.seleceKeyById(129)
    #     if appkey != 1:
    #         keyDome.Token(appkey, access_token)'''

    # 查询时间凭证
    # selTime.selectTime(access_token)

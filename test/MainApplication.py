import numpy
import Select_Key_Random as selKey
import Key_Demo_Token as keyDome
import App_and_Key_Service as testApp
import testUser as addUser
import Login_Token as loginToken
from faker import Faker
fake = Faker("zh_CN")
import string
import random
import SelectTime as selTime


phone = fake.phone_number()
email = fake.email()
# phone = '13438160279'
# password = "123456q"

password = ''
for i in range(numpy.random.randint(8, 16)):
    password += random.choice(string.digits + string.ascii_letters)
sum = 10

if __name__ == '__main__':

    addUser.AddUser(phone, email, password)
    username = phone
    access_token = 'Bearer' + loginToken.get_access_token(username, password)
    testApp.app_And_key(sum, access_token)
    #
    # for i in range(1):
    #     radAppId = numpy.random.randint(1, sum)
    #     appkey = selKey.seleceKeyById(129)
    #     if appkey != 1:
    #         keyDome.Token(appkey, access_token)

    selTime.selectTime(access_token)
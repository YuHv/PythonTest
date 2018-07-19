import numpy
import Select_Key_Random as selKey
import Key_Demo_Token as keyDome
import App_and_Key_Service as testApp
import testUser as addUser
import Login_Token as loginToken

phone = "17828019325"
email = "lx1186998828@qq.com"
password = "pwd123123"
sum = 100

if __name__ == '__main__':

    addUser.AddUser(phone, email, password)
    username = phone
    access_token = 'Bearer' + loginToken.get_access_token(username, password)
    testApp.app_And_key(sum, access_token)

    for i in range(10):
        radAppId = numpy.random.randint(1, sum)
        appkey = selKey.seleceKeyById(radAppId)
        if appkey != 1:
            keyDome.Token(appkey, access_token)

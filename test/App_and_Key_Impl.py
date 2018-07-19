import json
import requests
import random
import numpy
import Login_Token as loginToken
from faker import Factory

fake = Factory().create('zh_CN')

#
# access_token = 'Bearer'+loginToken.get_access_token()
# url = "http://10.25.127.116:8788/app"
url = "http://10.25.128.26:9999/front/app/app"
# headers = {'Content-Type': 'application/json', 'Authorization': access_token}
# headers1 = {'Authorization': access_token}
# headers2 = {'Content-Type': 'multipart/form-data'}
# headers3 = {'Content-Type': 'application/json'}


def choice_gen():
    """随机选取平台类型"""
    choices = ["windows", "web", "Android"]
    choiceGen = factory_choice_generator(choices)()
    return next(choiceGen)


def random_name():
    """随机姓名"""
    return fake.name()


def random_str(min_chars=1, max_chars=5):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def factory_choice_generator(values):
    """ 返回一个生成器函数，调用这个函数产生生成器，从给定的list中随机取一项。 """

    def choice_generator():
        my_list = list(values)
        while True:
            yield random.choice(my_list)

    return choice_generator


def ipWhitelist():
    """随机生成白名单"""
    return str(numpy.random.randint(0, 100)) + "." + str(numpy.random.randint(0, 100)) + "." + str(
        numpy.random.randint(0, 100)) + "." + str(numpy.random.randint(0, 100))


def listApp(access_token):
    headers1 = {'Authorization': access_token}
    r_app_list = requests.get(url, headers=headers1)
    data = r_app_list.json()
    return data


def addApp(sum, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    for i in range(sum):
        param = {"appName": random_name() + "的应用" + str(numpy.random.randint(0, 50000)) + random_str(),
                 "appType": numpy.random.randint(0, 3)}
        r_create_app = requests.post(url, headers=headers, data=json.dumps(param))
        data = r_create_app.json()
    return data


def updateApp(sum, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    for i in range(sum):
        param = {"appId": numpy.random.randint(1, sum),
                 "appName": "编辑app" + str(numpy.random.randint(0, 50000)) + random_str(),
                 "appType": numpy.random.randint(0, 3)}
        r_create_app = requests.put(url, headers=headers, data=json.dumps(param))
        data = r_create_app.json()
    return data


def addKey(sum, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    for i in range(sum):
        param = {"appId": numpy.random.randint(1, sum),
                 "keyName": random_name() + "的key" + str(numpy.random.randint(0, 50000)) + random_str(),
                 "platform": choice_gen(),
                 "ipWhitelist": ipWhitelist()}
        r_create_key = requests.post(url + "/key", headers=headers, data=json.dumps(param))
        data = r_create_key.json()
    return data


def updateKey(sum, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    for i in range(sum):
        param = {"keyId": numpy.random.randint(1, sum),
                 "keyName": "编辑key" + str(numpy.random.randint(0, 50000)) + random_str(),
                 "platform": choice_gen(),
                 "ipWhitelist": ipWhitelist()}
        r_update_key = requests.put(url + "/key", headers=headers, data=json.dumps(param))
        data = r_update_key.json()
    return data


def refresh(sum, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    for i in range(sum):
        param = {"keyId": numpy.random.randint(1, sum)}
        r_refresh_key = requests.put(url + "/key/refresh", headers=headers, params=param)
        data = r_refresh_key.json()
    return data


def deleteKey(sum, access_token):
    headers1 = {'Authorization': access_token}
    for i in range(sum):
        param = {"keyId": numpy.random.randint(1, sum)}
        r_delete_key = requests.delete(url + "/key", headers=headers1, params=param)
        data = r_delete_key.json()
    return data


def deleteApp(sum, access_token):
    headers1 = {'Authorization': access_token}
    for i in range(sum):
        param = {"appId": numpy.random.randint(1, sum)}
        r_delete_app = requests.delete(url, headers=headers1, params=param)
        data = r_delete_app.json()
    return data

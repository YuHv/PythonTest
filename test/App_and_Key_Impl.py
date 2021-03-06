import json
import requests
import random
import numpy
from faker import Factory

fake = Factory().create('zh_CN')

url = "http://10.25.128.26/app"


def choice_gen():
    """随机选取平台类型"""
    choices = ["windows", "web", "Android"]
    choiceGen = factory_choice_generator(choices)()
    return next(choiceGen)


def random_name():
    """随机姓名"""
    return fake.name()


def random_str(min_chars=1, max_chars=3):
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
    return fake.ipv4(network=False)


def listApp(access_token):
    headers1 = {'Authorization': access_token}
    r_app_list = requests.get(url, headers=headers1)
    data = r_app_list.json()
    return data


def addApp(access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    param = {"appName": "新应用" + str(numpy.random.randint(0, 50)) + random_str(),
             "appType": numpy.random.randint(0, 3)}
    r_create_app = requests.post(url, headers=headers, data=json.dumps(param))
    data = r_create_app.json()
    return data


def updateApp(appId, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    param = {"appId": appId,
             "appName": "编辑app" + str(numpy.random.randint(0, 50)) + random_str(),
             "appType": numpy.random.randint(0, 3)}
    r_create_app = requests.put(url, headers=headers, data=json.dumps(param))
    data = r_create_app.json()
    return data


def addKey(appId, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    param = {"appId": appId,
             "keyName": "新key" + str(numpy.random.randint(0, 50)) + random_str(),
             "platform": choice_gen(),
             "ipWhitelist": ipWhitelist()}
    r_create_key = requests.post(url + "/key", headers=headers, data=json.dumps(param))
    data = r_create_key.json()
    return data


def updateKey(keyId, access_token):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}

    param = {"keyId": keyId,
             "keyName": "编辑key" + str(numpy.random.randint(0, 50)) + random_str(),
             "platform": choice_gen(),
             "ipWhitelist": ipWhitelist()}
    r_update_key = requests.put(url + "/key", headers=headers, data=json.dumps(param))
    data = r_update_key.json()
    return data


def refresh(keyId, access_token, email_code):
    headers = {'Content-Type': 'application/json', 'Authorization': access_token}
    param = {"keyId": keyId, "validateCode": email_code}
    r_refresh_key = requests.put(url + "/key/refresh", headers=headers, params=param)
    data = r_refresh_key.json()
    return data


def deleteKey(keyId, access_token, email_code):
    headers1 = {'Authorization': access_token}

    param = {"keyId": keyId, "validateCode": email_code}
    r_delete_key = requests.delete(url + "/key", headers=headers1, params=param)
    data = r_delete_key.json()
    return data


def deleteApp(appId, access_token, email_code):
    headers1 = {'Authorization': access_token}
    param = {"appId": appId, "validateCode": email_code}
    r_delete_app = requests.delete(url, headers=headers1, params=param)
    data = r_delete_app.json()
    return data

import json
import string
import requests
import random
import numpy
from faker import Faker
fake = Faker("zh_CN")


def AddUser(phone, email, password):
    url = "http://10.25.128.26/reg"
    # url = "http://localhost:8788/reg"
    headers = {'Content-Type': 'application/json'}

    # 发送手机验证码
    r_phone = requests.get(url + "/" + phone)
    phone_code = r_phone.headers.get('code')  # 从response hearders中获取手机验证码
    data = r_phone.json()
    print("------------------------------发送手机验证码------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    # 注册模块
    # 生成用户
    param = {
        "phone": phone,
        "validateCode": phone_code,
        "userType": numpy.random.randint(0, 3),
        "password": password
    }
    r_register = requests.post(url, headers=headers, data=json.dumps(param))
    data = r_register.json()
    user_id = data.get('data').get('userId')  # 获取userId
    print("------------------------------添加用户接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    # choise = numpy.random.randint(1, 21)
    #
    # if choise < 21:
    # 上传营业执照
    files = {"license": open(r"F:\norecord.png", 'rb').read()}
    param = {"userId": user_id}
    r_upLoad = requests.post(url + "/upload", data=param, files=files)
    data = r_upLoad.json()
    print("------------------------------上传营业执照------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    # 发送邮箱验证码
    param = {'email': email}
    r_email = requests.get(url + "/checkemail/" + user_id, params=param)
    data = r_email.json()
    email_code = r_email.headers.get('code')  # 从response hearders中获取邮箱验证码
    print("------------------------------发送邮箱验证码------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    # 更新用户信息
    companyNo = ''
    for i in range(18):
        companyNo += random.choice(string.ascii_uppercase + string.digits)
    param = {
        "adminName": fake.name(),
        "companyName": fake.company(),
        "companyNo": companyNo,
        "email": email,
        "validateCode": email_code
    }
    r_update_user = requests.put(url + "/" + user_id, headers=headers, data=json.dumps(param))
    data = r_update_user.json()
    print("------------------------------更新用户信息------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

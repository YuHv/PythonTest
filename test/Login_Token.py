import json

import requests

# if __name__ == '__main__':


def get_access_token_nuerpwd(username, password):

    url = "http://10.25.128.26/userauth/oauth/token"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Authorization': "Basic cGlnOnBpZw==",
        'Cache-Control': "no-cache",
        'Postman-Token': "72ba7d8f-5553-4288-b94b-8c81289619b3"
        }
    param = {"username": username,
             "password": password,
             "scope": "server",
             "grant_type": "password"}

    # 获取登录Token
    r_loginToken = requests.post(url, headers=headers, params=param)
    data = r_loginToken.json()
    print("------------------------------获取登录Token------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    return data.get("access_token")


def get_access_token_phone(username):

    url = "http://10.25.128.26:3006/mobile/token"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'Authorization': "Basic cGlnOnBpZw==",
        'Cache-Control': "no-cache",
        'Postman-Token': "72ba7d8f-5553-4288-b94b-8c81289619b3"
        }
    param = {"mobile": username,
             "scope": "server",
             "grant_type": "mobile",
             "scope":"server"}

    # 获取登录Token
    r_loginToken = requests.post(url, headers=headers, params=param)
    data = r_loginToken.json()
    print("------------------------------获取登录Token------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    return data.get("access_token")
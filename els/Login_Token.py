import json

import requests

url = "http://10.25.128.26:3006/oauth/token"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n17828019325\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\npassword\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"scope\"\r\n\r\nserver\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n123456q\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Authorization': "Basic cGlnOnBpZw==",
    'Cache-Control': "no-cache",
    'Postman-Token': "bf9c7b32-abe4-4218-8265-2c2b9f6d9d10"
    }


def login():
    response = requests.request("POST", url, data=payload, headers=headers)

    data = response.json()
    print("------------------------------获取登录Token------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


if __name__ == '__main__':
    login()
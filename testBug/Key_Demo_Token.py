import json
from _sha256 import sha256
import requests
import base64
from faker import Factory

fake = Factory().create('zh_CN')


def random_str(min_chars=1, max_chars=3):
    """长度在最大值与最小值之间的随机字符串"""
    return fake.pystr(min_chars=min_chars, max_chars=max_chars)


def Token(appkey, app_secret):

    encode_str = base64.b64encode((str(appkey) + ":" + app_secret).encode('utf-8'))
    base64_str = str(encode_str, 'utf-8')
    authorization = "Basic " + base64_str
    print(authorization)
    #
    # print(authorization)

    #
    # 获取access_token
    # param = {"grant_type": "client_credentials", "scope": "all"}
    param = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"grant_type\"\r\n\r\nclient_credentials\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    r_header = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        "Authorization": authorization}
    # http://10.25.128.26:3006/oauth/token      http://10.25.128.26:8080/api/v1/token
    rq_get_access_token = requests.post("http://10.25.128.26:4013/oauth/token", headers=r_header, data=param)
    data = rq_get_access_token.json()
    print("------------------------------获取access_token接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    #
    # 生成app_secret_token
    app_secret_token = 'bearer' + data.get("access_token")
    rid = random_str()
    print(rid)
    sha_256 = sha256()
    sha_256.update(str.encode(rid))
    rid = sha_256.hexdigest()

    print(rid)
    #
    # 获取时间凭证接口
    param = {"rid": rid}
    header = {
         'Authorization': app_secret_token
    }
    # http://10.25.128.26:8080/api/v1/attestation/get   /api/v2/   http://10.25.128.26/timelicense
    rq_get_time = requests.post("http://10.25.128.26:9966/attestation/attestation/get", data=param, headers=header)
    data = rq_get_time.json()
    print("------------------------------获取时间凭证接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
# #
#
# if __name__ == '__main__':
#     # token = "eyJhcHBLZXlpZCI6MSwic2NvcGUiOlsicmVhZCJdLCJhcHBJZCI6MTksImV4cCI6MTUzMzA2MzIxNiwiQXBwU2VjcmV0IjoiM09vQ096Uld5U29icGFLa1FKM0RIVjNmQ205eFZKTlQiLCJ1c2VySWQiOjE0LCJqdGkiOiI4ODNmMWNmOC03MzFhLTQ1ZTItYmI2MS02Yjc4ODcwMzQ3NmMiLCJjbGllbnRfaWQiOiJUVEFTWU1EUlNjSU83clFtc2x5USJ9"
#     Token("TTASIipBxpnuMf0Ha1Xq","1")
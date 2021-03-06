import json
from _sha256 import sha256
import App_and_Key_Impl as app
import requests
import base64


def Token(appkey, login_token):

    # 通过APPKey获取appsecret
    headers = {'Content-Type': 'application/json', 'Authorization': login_token}
    param = {"appkey": appkey}
    r_app_secret = requests.get("http://10.25.128.26/app/appkey", headers=headers, params=param)
    data = r_app_secret.json()
    print("------------------------------获取appsecret接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    #
    # 生成appkey token的header
    app_secret = data.get("appsecret")
    encode_str = base64.b64encode((str(appkey) + ":" + app_secret).encode('utf-8'))
    base64_str = str(encode_str, 'utf-8')
    authorization = "Basic " + base64_str
    #
    # print(authorization)

    #
    # 获取access_token
    param = {"grant_type": "client_credentials", "scope": "all"}
    r_header = {"Authorization": authorization}
    # http://10.25.128.26:3006/oauth/token      http://10.25.128.26:8080/api/v1/token
    rq_get_access_token = requests.post("http://10.25.128.26:8080/api/v1/token", headers=r_header, data=param)
    data = rq_get_access_token.json()
    print("------------------------------获取access_token接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    #
    # 生成app_secret_token
    app_secret_token = data.get("access_token")
    rid = app.random_str()
    sha_256 = sha256()
    sha_256.update(str.encode(rid))
    rid = sha_256.hexdigest()

    #
    # 获取时间凭证接口
    param = {"rid": rid, "access_token": app_secret_token}
    rq_get_time = requests.post("http://10.25.128.26:8080/api/v1/attestation/get", data=param)
    data = rq_get_time.json()
    print("------------------------------获取时间凭证接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
#
#
# if __name__ == '__main__':
#     # token = "eyJhcHBLZXlpZCI6MSwic2NvcGUiOlsicmVhZCJdLCJhcHBJZCI6MTksImV4cCI6MTUzMzA2MzIxNiwiQXBwU2VjcmV0IjoiM09vQ096Uld5U29icGFLa1FKM0RIVjNmQ205eFZKTlQiLCJ1c2VySWQiOjE0LCJqdGkiOiI4ODNmMWNmOC03MzFhLTQ1ZTItYmI2MS02Yjc4ODcwMzQ3NmMiLCJjbGllbnRfaWQiOiJUVEFTWU1EUlNjSU83clFtc2x5USJ9"
#     Token("TTASIipBxpnuMf0Ha1Xq","1")
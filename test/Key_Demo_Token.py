import json
from _sha256 import sha256
import App_and_Key_Impl as app
import requests
import base64


def Token(appkey, login_token):
    headers = {'Content-Type': 'application/json', 'Authorization': login_token}
    param = {"appkey": appkey}
    r_app_secret = requests.get("http://10.25.128.26:9999/front/app/appkey", headers=headers, params=param)
    data = r_app_secret.json()
    print("获取appsecret接口--------------------------------------------------------------")
    # print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    print(data)
    app_secret = data.get("appsecret")
    print("appid:appsecre的值：" + str(appkey) + ":" + app_secret)
    # 将mystr转换为base64编码
    # authorization = "Basic "+binascii.a2b_base64(str(app_id)+":"+app_secret)

    encode_str = base64.b64encode((str(appkey) + ":" + app_secret).encode('utf-8'))
    base64_str = str(encode_str, 'utf-8')
    print("base64编码：" + base64_str)
    authorization = "Basic " + base64_str
    print("authorization的值：" + authorization)

    param = {"grant_type": "client_credentials"}
    r_header = {"Authorization": authorization}
    rq_get_access_token = requests.post("http://10.25.128.26:8080/api/v1/token", headers=r_header, data=param)
    data = rq_get_access_token.json()
    print("获取access_token接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    app_secret_token = data.get("access_token")
    print(app_secret_token)

    rid = app.random_str()
    sha_256 = sha256()
    sha_256.update(str.encode(rid))
    rid = sha_256.hexdigest()

    param = {"rid": rid, "access_token": app_secret_token}
    rq_get_time = requests.post("http://10.25.128.26:8080/api/v1/attestation/get", data=param)
    data = rq_get_time.json()
    print("获取时间凭证接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))


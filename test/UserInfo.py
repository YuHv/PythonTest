import json

import requests

url = "http://10.25.128.26/user"


def userInfo(access_token):
    headers = {
        'Authorization': access_token,
        'Cache-Control': "no-cache",
        'Postman-Token': "7ec4df3b-4318-4074-af4d-1c2ab02a7fbe"
    }

    r_update_user = requests.get(url, headers=headers)
    data = r_update_user.json()
    print("------------------------------当前用户信息------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

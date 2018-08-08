import json
import App_and_Key_Impl as app
import numpy
import Key_Demo_Token as keyDome
import requests


def app_And_key(sum, access_token):
    # 应用管理模块

    # headers = {'Authorization': access_token}
    # r_app_list = requests.get("http://10.25.128.26/user/appemail", headers=headers)
    # email_code = r_app_list.headers.get('code')  # 从response hearders中获取邮箱验证码
    # print("++++++++++++++++++++++++++++验证码++++++++++++++" + email_code)
    for i in range(sum):

        addApp_c = numpy.random.randint(1, 3)
        updateApp_c = numpy.random.randint(1, 4)

        if addApp_c == 1:
            # 创建新应用
            data = app.addApp(access_token)
            print("------------------------------创建新应用接口------------------------------")
            print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
            appId = data.get("data").get("appId")

            if updateApp_c == 1:
                # 更新应用
                data = app.updateApp(appId, access_token)
                print("------------------------------更新应用接口------------------------------")
                print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
            if updateApp_c == 2:
                # 删除应用
                data = app.deleteApp(appId, access_token, email_code)
                print("------------------------------删除应用接口------------------------------")
                print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
            else:
                print()

            for j in range(sum):
                addKey_c = numpy.random.randint(1, 3)
                updateKey_c = numpy.random.randint(1, 5)
                if addKey_c == 1:
                    # 创建新Key
                    data = app.addKey(appId, access_token)
                    print("------------------------------创建新key接口------------------------------")
                    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
                    appkey = data.get("data").get("appKey")
                    keyDome.Token(appkey, access_token)
                    keyId = data.get("data").get("keyId")

                    if updateKey_c == 1:
                        # 编辑key
                        data = app.updateKey(keyId, access_token)
                        print("------------------------------编辑key接口------------------------------")
                        print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
                    elif 3 <= updateKey_c == 2:
                        # 重置key
                        data = app.refresh(keyId, access_token, email_code)
                        print("------------------------------重置key接口------------------------------")
                        print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
                        appkey = data.get("data").get("appKey")
                        keyDome.Token(appkey, access_token)
                    elif updateKey_c == 3:
                        # 删除key
                        data = app.deleteKey(keyId, access_token, email_code)
                        print("------------------------------删除key接口------------------------------")
                        print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
                    else:
                        print()

    # 获取应用列表
    data = app.listApp(access_token)
    print("------------------------------获取应用列表接口------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

# if __name__ == '__main__':
#     access_token='Bearer'+"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSB0dGFzIiwidXNlcl9uYW1lIjoiMTc4MjgwMTkzMjUiLCJzY29wZSI6WyJzZXJ2ZXIiXSwiZXhwIjoxNTMyMDI2MzQ4LCJhdXRob3JpdGllcyI6WyJmcm9udHVzZXIiLCJST0xFX1VTRVIiXSwianRpIjoiZDczODBkZmYtZWY2Ni00ODJhLTkxMDAtNTQ5NTc3NzMzNDdkIiwiY2xpZW50X2lkIjoicGlnIn0.fAZ0hpwUNFY8Wk3sOp44A0kP9jCPiW4FRuh5B_nX9OM"
#     sum = 2
#     app_And_key(sum, access_token)

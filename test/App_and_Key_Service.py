import json
import App_and_Key_Impl as app


def app_And_key(sum, access_token):
    # 应用管理模块
    # 获取应用列表
    # data = app.listApp(access_token)
    # print("获取应用列表接口--------------------------------------------------------------")
    # print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # 创建新应用
    data = app.addApp(sum, access_token)
    print("创建新应用接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    # 更新应用
    data = app.updateApp(sum, access_token)
    print("更新应用接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # 创建新Key
    data = app.addKey(sum, access_token)
    print("创建新key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # 编辑key
    data = app.updateKey(sum, access_token)
    print("编辑key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # 重置key
    data = app.refresh(sum, access_token)
    print("重置key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # 删除key
    data = app.deleteKey(sum, access_token)
    print("删除key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # 删除应用
    data = app.deleteApp(sum, access_token)
    print("删除应用接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
#
#
# if __name__ == '__main__':
#     access_token='Bearer'+"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSB0dGFzIiwidXNlcl9uYW1lIjoiMTc4MjgwMTkzMjUiLCJzY29wZSI6WyJzZXJ2ZXIiXSwiZXhwIjoxNTMyMDI2MzQ4LCJhdXRob3JpdGllcyI6WyJmcm9udHVzZXIiLCJST0xFX1VTRVIiXSwianRpIjoiZDczODBkZmYtZWY2Ni00ODJhLTkxMDAtNTQ5NTc3NzMzNDdkIiwiY2xpZW50X2lkIjoicGlnIn0.fAZ0hpwUNFY8Wk3sOp44A0kP9jCPiW4FRuh5B_nX9OM"
#     sum = 2
#     app_And_key(sum, access_token)

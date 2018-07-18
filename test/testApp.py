import json
import AppH as app


def app_And_key(sum):

    # 应用管理模块
    # 获取应用列表
    # data = app.listApp()
    # print("获取应用列表接口--------------------------------------------------------------")
    # print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

    # 创建新应用
    data = app.addApp(sum)
    print("创建新应用接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # # 更新应用
    data = app.updateApp(sum)
    print("更新应用接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # # 创建新Key
    data = app.addKey(sum)
    print("创建新key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # # 编辑key
    data = app.updateKey(sum)
    print("编辑key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # # 重置key
    data = app.refresh(sum)
    print("重置key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # # 删除key
    data = app.deleteKey(sum)
    print("删除key接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    #
    # # 删除应用
    data = app.deleteApp(sum)
    print("删除应用接口----------------------------------------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

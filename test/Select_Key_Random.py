import pymysql.cursors

# 连接MySQL数据库
from asn1crypto._ffi import null

connection = pymysql.connect(host='10.25.128.24', port=3306, user='root', password='123456',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()


def seleceKeyById(keyId):
    # 创建sql 语句，并执行
    sql = "select appkey from `app`.key_info where key_id = %d;" % keyId
    cursor.execute(sql)

    # 提交SQL
    # connection.commit()
    rows = cursor.fetchall()
    if rows:
        print("随机查询到的 appkey" + rows[0].get("appkey"))
        return rows[0].get("appkey")
    else:
        return 1
    # print(rows)

    # for dr in rows:
    #     print(dr)

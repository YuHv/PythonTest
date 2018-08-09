import pymysql.cursors

import Key_Demo_Token
# 连接MySQL数据库
from asn1crypto._ffi import null

connection = pymysql.connect(host='mysql.chinattas.cn', port=3306, user='upp', password='Aa789789',
                             charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

# 通过cursor创建游标
cursor = connection.cursor()


def seleceKeyById(keyId):
    # 创建sql 语句，并执行
    sql = "select appkey, appsecret from `upp`.key_info where key_id = %d;" % keyId
    cursor.execute(sql)

    # 提交SQL
    # connection.commit()
    rows = cursor.fetchall()
    if rows:
        # print("随机查询到的 appkey" + rows[0].get("appkey"))
        return rows
    else:
        return 1
    # print(rows)

    # for dr in rows:
    #     print(dr)


if __name__ == '__main__':
     # for i in range(20):
    rows = seleceKeyById(18)
    appkey = rows[0].get("appkey")
    appsecret = rows[0].get("appsecret")
    print(rows[0].get("appkey"), rows[0].get("appsecret"))
    Key_Demo_Token.Token(appkey, appsecret)
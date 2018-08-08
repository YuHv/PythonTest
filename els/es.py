import json

import numpy
import requests
import time
import datetime


# print (t)                       #原始时间数据
# print (int(t))                  #秒级时间戳
# print (int(round(t * 1000)))    #毫秒级时间戳
#
# nowTime = lambda:int(round(t * 1000))
# print (nowTime());              #毫秒级时间戳，基于lambda
#
# print (datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))   #日期格式化
url = "http://10.25.127.40:9200/test/attestation/"
headers = {'Content-Type': "application/json"}

def es(i):
    ts = int(time.time())
    if ts%2 ==0 :
        j = ts
    param = {"vid": "vid"+str(11111111111111),
             "extend": "extend"+str(12),
             "offset": str(23),
             "transid": str(32),
             "oid": "old"+str(3),
             "rid": "rid"+str(1),
             "aid": "Aid"+str(2),
             "userid": str(numpy.random.randint(1, 10)),
             "applytime": datetime.datetime.utcnow().isoformat(),
             "ts": time.time(),#int(round(time.time() * 1000)),
             "desc": "time_info"}
    print(datetime.datetime.utcnow().isoformat())
    r_delete_key = requests.put(url + str(i), headers=headers, data=json.dumps(param))
    # data = r_delete_key.json()
    # print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))
    # return j


if __name__ == '__main__':
    for i in range (500):
        es(i+1)
        print(i)
    print("end")
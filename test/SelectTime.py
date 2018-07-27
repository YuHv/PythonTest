import json

import requests

url = "http://10.25.128.26/time/timelicense"


def selectTime(access_token):
    # if __name__ == '__main__':
    # print(access_token)
    # access_token = "BearereyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSB0dGFzIiwidXNlcl9uYW1lIjoiMTM0MzgxNjAyNzkkMSIsInNjb3BlIjpbInNlcnZlciJdLCJleHAiOjE1MzIxMDc3NDAsImF1dGhvcml0aWVzIjpbImZyb250dXNlciIsIlJPTEVfVVNFUiJdLCJqdGkiOiI0Y2FkYmY2Yi0wZjE2LTQwNmQtOGE0Yi1kYTZlYzYzYjcwMGMiLCJjbGllbnRfaWQiOiJwaWcifQ.Xeo7djXfK2wqVndo00L4pR7jY_1q8ZZbqFbNDAIl-DY"

    param = {"page": "1", "limit": "10"}

    headers = {
        'Authorization': access_token,
        'Cache-Control': "no-cache",
        'Postman-Token': "49f46373-fad2-4a6c-92ec-fd179263d658"
    }

    r_selectTime = requests.get(url, headers=headers, params=param)
    data = r_selectTime.json()
    print("------------------------------查询时间凭证------------------------------")
    print(json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False))

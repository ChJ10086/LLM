import http.client
import json

'''Help Methods'''
def chat(content, model = 'gpt-4o-mini'):
    conn = http.client.HTTPSConnection()
    payload = json.dumps({
    "model": f'{model}',
    "messages": [
        {
            "role": "user",
            "content": f'{content}'
        }
    ]
    })

    key = get_key()
    headers = {
    'Authorization': f'{key}',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/v1/chat/completions", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    return data.decode("utf-8")
    



'''Help Methods'''

def get_api():
    return 'open.xiaojingai.com'

def get_key():
    with open('data/apikey.txt', 'r') as key_file:
        key = key_file.read()
        return key.strip()
# test.py

import http.client
import json

from config import Config

def request(content, role = 'user', messages = None, model_name = 'gpt-4o-mini'):
    conn = http.client.HTTPSConnection("open.xiaojingai.com")

    if messages:
        payload = json.dumps(messages)
    else:
        model = Config.model_mappings[model_name]
        payload = json.dumps({
            'model': model,
            'messages': [{'role': role, 'content': content}]
        })
    headers = {
    'Authorization': f'{Config.key}',
    'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
    'Content-Type': 'application/json'
    }
    conn.request('POST', '/v1/chat/completions', payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode('utf-8')

def parse_response_contents(response):
    choices = json.loads(response)['choices']
    return [choice['message']['content'] for choice in choices]

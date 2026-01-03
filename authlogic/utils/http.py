import requests

def send(method, url, headers=None, cookies=None, json=None):
    return requests.request(
        method=method,
        url=url,
        headers=headers or {},
        cookies=cookies or {},
        json=json,
        timeout=8,
        allow_redirects=False
    )

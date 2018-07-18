import os
import json
from urllib3 import PoolManager,exceptions

def get_all():
    http = PoolManager()
    try :
        r = http.request('GET', 'http://ipinfo.io')
    except exceptions.MaxRetryError:
        return None
    json_resp = json.loads(r.data.decode('utf-8'))
    return json_resp

def get_country_code():
    json_resp['country']

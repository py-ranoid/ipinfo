import json
import argparse
from urllib3 import PoolManager,exceptions
from pkg_resources import resource_filename


def get_all():
    http = PoolManager()
    try :
        r = http.request('GET', 'http://ipinfo.io')
    except exceptions.MaxRetryError:
        return None
    json_resp = json.loads(r.data.decode('utf-8'))
    return json_resp

def get_country_code():
    return get_all()['country']

def get_country_name(code=None):
    code = get_country_code() if code is None else code
    with open(resource_filename(__name__,'country_names.json')) as f:
        names = json.loads(f)
    return names[code]

def get_city():
    return get_all()['city']

def get_region():
    return get_all()['region']

def get_ip():
    return get_all()['ip']

def get_hostname():
    return get_all()['hostname']

def get_locstring():
    resp = get_all()
    cname = get_country_name(resp['country'])
    locstring = resp['region']+', '+resp['city']+', '+cname
    return locstring

def get_coords():
    return get_all()["loc"]

# ipinfo
Module to fetch information about user using IP address<br>*Python wrapper for `ipinfo.io` API*

## Installing
```
  pip3 install .
```

## Options

    cn : Get Country Name only
    cc : Get Country Code only
    ct : Get City only
    rg : Get Region only
    ls : Get location as a string
    lc : Get coordinates
    ip : Get IP Address only
    hn : Get Host Name only
    a  : Get all details.

## Example
### CLI

```
  $ python3 -m ipinfo
  {'loc': '13.0833,80.2833', 'country': 'IN', 'org': 'AS24309 Atria Convergence Technologies Pvt. Ltd.  Broadband Internet Service Provider INDIA', 'region': 'Tamil Nadu', 'city': 'Chennai', 'ip': '123.123.123.123', 'postal': '600003'}

  $ python3 -m ipinfo cc
  IN

  $ python3 -m ipinfo ls
  Tamil Nadu, Chennai, India

```
### `ipinfo` Module
```
from ipinfo.ipinfo import get_country_name,get_all

print (get_country_name())
# Chennai

print (get_all())
# {'city': 'Chennai',
# 'region': 'Tamil Nadu',
# 'ip': '123.123.123.123',
# 'hostname': 'broadband.actcorp.in',
# 'org': 'AS24309 Atria Convergence Technologies Pvt. Ltd.  Broadband Internet Service Provider INDIA',
# 'postal': '600003',
# 'country': 'IN',
# 'loc': '13.0833,80.2833'}
```

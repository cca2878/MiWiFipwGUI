import hashlib
from hashlib import md5

# credit goes to zhoujiazhao:
# <a href="https://blog.csdn.net/zhoujiazhao/article/details/102578244" target="_blank">https://blog.csdn.net/zhoujiazhao/article/details/102578244</a>

salt = {'r1d': 'A2E371B0-B34B-48A5-8C40-A7133F3B5D88',
        'others': 'd44fb0960aa0-a5e6-4a30-250f-6d2df50a'}


def get_salt(sn):
    if "/" not in sn:
        return salt["r1d"]

    return "-".join(reversed(salt["others"].split("-")))


def calc_passwd(sn):
    passwd = sn + get_salt(sn)
    m = md5(passwd.encode())
    return m.hexdigest()[:8]
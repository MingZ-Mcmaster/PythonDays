#! _*_ coding:utf-8 _*_
# __author__ = "Ming"

import json
acc_dict = {
    'id':1234,
    'password':'abc',
    'credit':15000,
    'balance':15000,
    'enroll_date':'2016-01-02',
    'expire_date':'2021-01-01',
    'pay_day':22,
    'status':0, # 0 = normal, 1 = locked, 2 = disabled
}

print(json.dumps(acc_dict))
#! _*_ coding:utf-8 _*_
# __author__ = "Ming"
import os
import sys
import logging

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASE = {
    'engine':'file_storage', # support mysql, postgresql in the future
    'name':'accounts',
    'path':f'{BASE_DIR}\db',
}

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction':'transactions.log',
    'access':'access.log',
}

TRANSACTION_TYPE = {
    'reply' : {'action':'plus', 'interest':0},
    'withdraw' : {'action':'minus', 'interest':0.05},
    'transfer' : {'action':'minus', 'interest':0.05},
    'consume' : {'action':'minus', 'interest':0},
}
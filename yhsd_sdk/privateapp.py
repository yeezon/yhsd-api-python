# coding: utf-8

'''
友好速搭私有应用方法
'''

import requests
import json

import config
import verify

def generate_token():
    '''
    生成商铺token
    '''
    params = {'grant_type': 'client_credentials'}
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': verify.private_app_authorization(config.AppKey, config.AppSecret),
    }
    r = requests.request(method='post', url=config.TokenUrl, data=params, headers=headers)
    if r.status_code != requests.codes.ok:
        return "Error:" + r.text
    return r.json()['token']


# coding: utf-8

'''
友好速搭开放应用方法
'''
import requests
import json

import config
import verify

def generate_token(auth_code, redirect_uri):
    '''
    获取token
    :param auth_code: 授权码
    :redirect_uri: 授权后重定向的链接
    :return: 返回商铺的token
    '''
    params = {
        'grant_type': 'authorization_code',
        'code': auth_code,
        'client_id': config.AppKey,
        'redirect_uri': redirect_uri,
    }
    r = requests.request(
        method='post',
        url=config.TokenUrl,
        data=params,
        headers={'Content-Type': "application/x-www-form-urlencoded"},
    )
    if r.status_code != requests.codes.ok:
        return "Error:" + r.text
    return r.json()['token']

def generate_authorize_url(redirect_url, shop_key, state=None):
    '''
    生成授权链接
    :param redirect_url: 授权成功后的跳转地址
    :param shop_key: 友好速搭的商铺唯一key
    :param state: 自定义参数，可选项
    :return: 返回用于授权的跳转链接
    '''
    redirect_data = {
        'response_type': 'code',
        'client_id': config.AppKey,
        'shop_key': shop_key,
        'scope': ','.join(config.AppScope),
        'redirect_uri': redirect_url,
    }
    if state:
        redirect_data['state'] = state
    qs = ''
    for k,v in redirect_data.items():
        qs += '%s=%s&' % (k, v)
    return config.AuthUrl + '?' + qs.rstrip('&')


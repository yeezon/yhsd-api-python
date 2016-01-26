# coding: utf-8

'''
友好速搭Python SDK API
'''

import requests
import json

import config
import verify

class Api(object):
    '''
    API类
    '''
    def __init__(self, token):
        '''
        api对象初始化
        :param token: 已授权店铺的token
        '''
        self._token = token
        self._get_header = {'X-API-ACCESS-TOKEN': self._token}
        self._post_header = dict(self._get_header)
        self._post_header['Content-Type'] = 'application/json'

    def get(self, path, **kwargs):
        '''
        get请求
        :param path: 请求的资源路径
        :param kwargs: 其他附加的HTTP参数列表（如header等）
        :return: response对象
        '''
        return requests.request(
            method='get',
            url=config.generate_api_url(path),
            headers=self._get_header,
            **kwargs
        )

    def _post(self, path, data=None, method='post', **kwargs):
        '''
        post, put, deleta等公用的内部方法
        '''
        post_data = data
        if post_data is not None:
            post_data = json.dumps(post_data)
        return requests.request(
            method=method,
            url=config.generate_api_url(path),
            data=post_data,
            headers=self._post_header,
            **kwargs
        )

    def post(self, path, data=None, **kwargs):
        '''
        post请求
        :param path: 请求的资源路径
        :param data: POST请求数据，为dict类型
        :param kwargs: 其他附加的HTTP参数列表（如header等）
        :return: response对象
        '''
        return self._post(path, data, 'post')

    def put(self, path, data=None, **kwargs):
        '''
        put请求
        :param path: 请求的资源路径
        :param data: PUT请求数据，为dict类型
        :param kwargs: 其他附加的HTTP参数列表（如header等）
        :return: response对象
        '''
        return self._post(path, data, 'put')

    def delete(self, path, data=None, **kwargs):
        '''
        delete请求
        :param path: 请求的资源路径
        :param data: DELETE请求数据，为dict类型
        :param kwargs: 其他附加的HTTP参数列表（如header等）
        :return: response对象
        '''
        return self._post(path, data, 'delete')


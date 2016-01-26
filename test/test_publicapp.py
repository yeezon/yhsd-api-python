# coding: utf-8

'''
私用应用单元测试类
'''

import sys
import unittest

sys.path.append('..')
from yhsd_sdk import config, publicapp, utils

import appconfig

class TestPrivateApp(unittest.TestCase):
    def setUp(self):
        utils.disable_urllib3_warning()
        config.AppKey = appconfig.AppKey
        config.AppSecret = appconfig.AppSecret
        config.AppScope = list(appconfig.AppScope)

    def test_generate_token(self):
        token = '93a4d98ab78843d2b9e7474436f2fe3c'
        code = 'a93cb80bcbbc45e2ae9af34593c213cc'
        redirect_url = 'http://localhost:8080/auth_confirm'
        self.assertEqual(token, publicapp.generate_token(code, redirect_url))

    def test_generate_authorize_url(self):
        url = 'https://apps.youhaosuda.com/oauth2/authorize?shop_key=3289572b75abe5aa618548f98d71a65e&scope=read_basic,write_basic,read_content,write_content&redirect_uri=http://localhost:8080/auth_confirm&response_type=code&client_id=5c768a6fe94f41a4a2465756383e745f'
        shop_key = '3289572b75abe5aa618548f98d71a65e'
        redirect_url = 'http://localhost:8080/auth_confirm'
        self.assertEqual(url, publicapp.generate_authorize_url(redirect_url, shop_key))

if __name__ == '__main__':
    unittest.main()

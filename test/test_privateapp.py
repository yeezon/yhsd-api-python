# coding: utf-8

'''
私用应用单元测试类
'''

import sys
import unittest

sys.path.append('..')
from yhsd_sdk import config, privateapp, utils

import appconfig

class TestPrivateApp(unittest.TestCase):
    def setUp(self):
        utils.disable_urllib3_warning()
        config.AppKey = appconfig.PrivateAppKey
        config.AppSecret = appconfig.PrivateAppSecret

    def test_generate_token(self):
        self.assertEqual(appconfig.PrivateAppToken, privateapp.generate_token())

if __name__ == '__main__':
    unittest.main()

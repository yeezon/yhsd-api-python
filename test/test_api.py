# coding: utf-8

'''
API单元测试类
'''

import sys
import unittest

sys.path.append('..')
from yhsd_sdk import api, utils

import appconfig

class TestPrivateApp(unittest.TestCase):
    def setUp(self):
        utils.disable_urllib3_warning()
        self._app = api.Api (appconfig.AppToken)

    def test_get(self):
        response = self._app.get('shop')
        self.assertIn(response.status_code, [200, 422])

    def test_put(self):
        params = {
            "redirect": {
                "path": "/12345",
                "target": "/blogs"
            }
        }
        response = self._app.put('redirects/1', params)
        self.assertIn(response.status_code, [200, 422])

    def test_post(self):
        params = {
            "redirect": {
                "path": "/12345",
                "target": "/blogs"
            }
        }
        response = self._app.post('redirects', params)
        self.assertIn(response.status_code, [200, 422])

    def test_delete(self):
        response = self._app.delete('redirects/1')
        self.assertIn(response.status_code, [200, 422])

if __name__ == '__main__':
    unittest.main()

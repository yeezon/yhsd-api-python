# coding: utf-8

'''
测试几个加密函数
'''
import sys
import unittest

sys.path.append('../yhsd_sdk/')
from verify import *

class TestVerify(unittest.TestCase):
    def test_private_app_authrization(self):
        key = 'a94a110d86d2452eb3e2af4cfb8a3828'
        secret = 'a84a110d86d2452eb3e2af4cfb8a3828'
        origin = 'Basic YTk0YTExMGQ4NmQyNDUyZWIzZTJhZjRjZmI4YTM4Mjg6YTg0YTExMGQ4NmQyNDUyZWIzZTJhZjRjZmI4YTM4Mjg='
        self.assertEqual (origin, private_app_authorization(key, secret))

    def test_ca_hamc_code(self):
        secret = 'hush'
        params = {
            "shop_key": "a94a110d86d2452eb3e2af4cfb8a3828",
            "code": "a84a110d86d2452eb3e2af4cfb8a3828",
            "account_id": "1",
            "time_stamp": "2013-08-27T13:58:35Z",
            "hmac": "a2a3e2dcd8a82fd9070707d4d921ac4cdc842935bf57bc38c488300ef3960726"
        }
        self.assertEqual (params['hmac'], cal_hmac_code(secret, params))

    def test_verify_webhook(self):
        body = "{\"created_at\":\"2014-08-28T17:28:13.301+08:00\",\"domain\":\"www.example.com\",\"enable_email_regist\":true,\"enable_mobile_regist\":true,\"enable_username_regist\":true,\"name\":\"TEST\",\"page_description\":\"\",\"page_title\":\"\",\"updated_at\":\"2015-07-27T13:58:14.607+08:00\",\"url\":\"http://www.example.com\",\"webhook_token\":\"906155047ff74a14a1ca6b1fa74d3390\"}"
        token = '906155047ff74a14a1ca6b1fa74d3390'
        hmac_value = 'NS0Wcz2CDgzI4+L9/UYdwaXpPI4As7VD+wKCRgKqNUo='
        self.assertTrue(hmac_value, verify_webhook(token, body, hmac_value))

    def test_aes_encode(self):
        secret = '095AE461E2554EED8D12F19F9662247E'
        s = '{"uid":"test@youhaosuda.com","type":"email","name":"test"}'
        origin = 'mJgEpH-ja_sBlYG_W3HcbekE_HP2yQVrlX2hu8AKM8F5JjPFTRYBwc62HGhCZgfyf3FxECC9u-tcnmsZcheENw=='
        self.assertEqual(aes_encode(secret, s), origin)

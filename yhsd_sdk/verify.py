# coding: utf-8

import base64
import hmac
import hashlib
import json

# 需要安装pycrypto包
from Crypto.Cipher import AES

def private_app_authorization(app_key, app_secret):
    """
    根据appkey和appsecret生成私用应用授权凭证信息。
    生成方法：
    将私有应用的凭证，包括 App Key 和 App Secret，使用:连接成字符串：key:secret，使用 Base64（RFC 4648），将字符串编码。编码后的字符串，放在Basic及空格后面，组成新的字符串
    """
    return "Basic " + base64.urlsafe_b64encode(app_key + ':' + app_secret)

def cal_hmac_code(app_secret, data):
    '''
    生成请求对应的HMAC串
    :param app_secret: 应用密钥
    :param data: 请求数据（dict类型）
    :return: 生成的hmac串
    '''
    params = dict(data)
    # 先排除hmac参数
    if 'hmac' in params:
        del params['hmac']
    # 按字母序重排序
    query_list = []
    for key in sorted(params.keys()):
        query_list.append('%s=%s' % (key, params[key]))
    # 重新拼接成字符串形式
    query_string = '&'.join(query_list)
    # 生成hmac串
    return hmac.new(app_secret, query_string, hashlib.sha256).hexdigest()

def verify_webhook(token, data, hmac_code):
    '''
    webhook验证
    :param token: 用于加密的商铺token
    :param data: webhook请求的body（通常为json串）
    :param hmac_code: webhook请求头里的X-YHSD-HMAC-SHA256值
    :return True or False
    '''
    return hmac_code == base64.b64encode(hmac.new(token, data, hashlib.sha256).digest())

def aes_encode(shop_secret, s, is_base64_encode=True):
    '''
    对第三方接入商铺信息进行AES加密
    :param shop_secret: 商店密钥
    :param s:请求字符串
    :param is_base64_encode: 是否对加密字符串进行base64加密，默认值为True
    :return: 返回处理过后的字符串
    '''
    bs = AES.block_size
    pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
    aes_key = shop_secret[:bs]
    aes_iv = shop_secret[bs:bs*2]
    aes_string = AES.new(aes_key, AES.MODE_CBC, aes_iv).encrypt(pad(s))
    if is_base64_encode:
        return base64.urlsafe_b64encode(aes_string)
    return aes_string

def generate_open_login_url(shop_url, shop_secret, userdata):
    '''
    生成第三方用户自动登陆链接
    :param shop_url: 商铺url
    :param shop_secret: 商铺的密钥
    :param userdata: 第三方用户信息(dict类型)
    :return: 自动登陆的url地址
    '''
    encode_string = aes_encode(shop_secret, json.dumps(userdata))
    return "%s/account/multipass/login/%s" % (shop_url, encode_string)

# coding: utf-8
import sys
sys.path.append('..')

from yhsd_sdk import config, verify, utils, api, publicapp
import appconfig
import web

# 测试使用
# 商铺第三方接入的密钥（需替换成真实商店数据）
ShopSecretForAutoLogin = 'B854816B00C74CD694E4952EEC173BEE'
ShopUrl = 'http://py.youhaovip.com'
ShopWebhookToken = '906155047ff74a14a1ca6b1fa74d3390'

'''
友好速搭应用Demo，支持
    授权登陆
    第三方自动登陆
    webhook
    ...
    等功能

使用方法：
1）安装web.py
    pip install web.py
2) 启动web服务
    python miniweb.py
'''

urls = (
    '/', 'Index',
    '/callback', 'Callback',
    '/auth_confirm', 'AuthConfirm',
    '/autologin', 'AutoLogin',
)

redirect_uri_on_auth = 'http://localhost:8080/auth_confirm'

class Index(object):
    def GET(self):
        return "Hello, My Friend"

class AutoLogin(object):
    def GET(self):
        '''
        模拟第三方自动登陆
        '''
        fake_data = {
            'uid': 'fakeuser@qq.com',
            'type': 'email',
            'name': 'fake',
        }
        web.seeother(verify.generate_open_login_url(ShopUrl, ShopSecretForAutoLogin, fake_data))

class AuthConfirm(object):
    def GET(self):
        '''
        授权成功（用户成功安装应用）
        '''
        data = web.input()
        if 'hmac' not in data or data['hmac'] != verify.cal_hmac_code(config.AppSecret, data):
            return 'hmac verify failed'
        auth_code = data['code']
        # 获取Token
        utils.disable_urllib3_warning()
        token = publicapp.generate_token(auth_code, redirect_uri_on_auth)
        return 'authcode=%s token=%s' % (auth_code, token)

class Callback(object):
    def GET(self):
        '''
        处理安装应用时验证请求
        '''
        data = dict(web.input())
        if 'hmac' not in data or data['hmac'] != verify.cal_hmac_code(config.AppSecret, data):
            return 'hmac verify failed'
        if 'shop_key' not in data:
            return 'shop_key requires'
        # 验证通过，重定向回友好速搭
        state = None
        if 'state' in data:
            state = data['state']
        auth_url = publicapp.generate_authorize_url(redirect_uri_on_auth, data['shop_key'], state)
        #print state, data['shop_key']
        #print auth_url
        web.seeother(auth_url)

    def POST(self):
        data = web.input()
        # webhook验证
        hmac_code = web.ctx.env.get('HTTP_X_YHSD_HMAC_SHA256', None)
        if not hmac_code or not verify.verify_webhook(ShopWebhookToken, web.data(), hmac_code):
            return 'webhook verify failed'
        # 删除应用
        if 'delete' == data.get('event', None):
            # do some logic of being deleted
            return 'delete app ok'
        return "Hello, Callback On Post"

if __name__ == "__main__":
    # 设置配置
    config.AppKey = appconfig.AppKey
    config.AppSecret = appconfig.AppSecret
    config.AppScope = list(appconfig.AppScope)
    app = web.application(urls, globals())
    app.run()

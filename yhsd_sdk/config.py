# coding: utf-8

# 友好速搭相关url配置
ApiUrl = "https://api.youhaosuda.com"
# api版本
ApiVersion = "v1"
# 获取token地址
TokenUrl = "https://apps.youhaosuda.com/oauth2/token"
# 获取授权码地址
AuthUrl = 'https://apps.youhaosuda.com/oauth2/authorize'

# 应用的key
AppKey = '这里填应用的App Key'
# 应用的密钥
AppSecret = '这里填应用的App Secret'
# 应用所需要的权限
AppScope = ['所需权限1', '所需权限2']

def generate_api_url(path):
    '''
    根据请求的资源路径生成对应的api链接地址
    '''
    return '/'.join((ApiUrl, ApiVersion, path.lstrip('/')))

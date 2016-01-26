# yhsd-api-python

友好速搭应用开发 Python SDK

## 安装

```python
pip install yhsd-sdk
```

或下载到本地后，手动安装

```python
# /path/to/file 为包解压之后的目录
pip install /path/to/file
```

## 使用方法

### 1）配置并创建App实例（如果是开放应用，则需要设置用用需要的权限列表）；

```python
# 配置文件config.py
# 应用的key
AppKey = '这里填应用的App Key'
# 应用的密钥
AppSecret = '这里填应用的App Secret'
# 应用所需要的权限
AppScope = ['所需权限1', '所需权限2']
```

### 2）获取授权Token（只需操作一次，永久生效）；

```python
# 获取私有应用token
token = privateapp.generate_token()

# 获取公有应用token
# 1) 生成授权链接并调整获取授权码。redirect_url为跳转链接；shop_key为商铺的唯一key
publicapp.generate_authorize_url (redirect_url, shop_key)
# 2) 根据返回的授权码获取Token。auth_code为返回的授权码；redirect_uri为跳转链接
token = publicapp.generate_token(auth_code, redirect_uri)
```

因为token是永久有效的，因此在第一次授权获取token后，可保存下来，以后直接使用。

### 3）调用封装好的API方法（更详细注释可以见代码内的注释）；

```python
# 使用token创建api对象
api = api.Api(token)

# 调用REST接口
api.get(path, **kwargs):
    '''
    get请求
    :param path: 请求的资源路径
    :param kwargs: 其他附加的HTTP参数列表（如header等）
    :return: response对象
    '''

api.put(path, data=None, **kwargs):
    '''
    put请求
    :param path: 请求的资源路径
    :param data: PUT请求数据，为dict类型
    :param kwargs: 其他附加的HTTP参数列表（如header等）
    :return: response对象
    '''

api.post(path, data=None, **kwargs):
    '''
    post请求
    :param path: 请求的资源路径
    :param data: POST请求数据，为dict类型
    :param kwargs: 其他附加的HTTP参数列表（如header等）
    :return: response对象
    '''

api.delete(path, data=None, **kwargs):
    '''
    delete请求
    :param path: 请求的资源路径
    :param data: DELETE请求数据，为dict类型
    :param kwargs: 其他附加的HTTP参数列表（如header等）
    :return: response对象
    '''
```

## 开放应用Demo
* test/miniweb.py
    * 基于web.py的一个简单的友好速搭应用demo。支持用户授权安装，交互数据验证，第三方自动登陆，webhook等功能

```python
'''
使用方法：
1）安装web.py
    pip install web.py
2) 启动web服务
    python miniweb.py
'''
```

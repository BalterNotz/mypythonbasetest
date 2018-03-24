#!/usr/bin/env python
# Python3

'''
网络爬虫
urllib的使用
代理的使用
'''

import urllib.request

googleip = 'http://88.191.249.182/'
baidu = 'http://www.baidu.com'
kitten = 'http://placekitten.com'

# response = urllib.request.urlopen(baidu)
#
# html = response.read()

# 下面从placekitten上面下载一个图片
request = urllib.request.Request('http://placekitten.com/g/500/600')
response = urllib.request.urlopen(request)
cat_img = response.read()
with open('cat_img.jpg', 'wb') as f:
    f.write(cat_img)

# 模拟浏览器进行操作
# 下面这个是失败的，因为这个接口里面有加salt和sign进行校验
youdaofanyiurl = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
data = {
    'action': 'FY_BY_CLICKBUTTION',
    'client': 'fanyideskweb',
    'doctype': 'json',
    'from': 'AUTO',
    'i': 'BalterNotz',
    'keyfrom': 'fanyi.web',
    'salt': '1516804271536',
    'sign': '102ad2ed17853333f7fd72b3c5717fdf',
    'smartresult': 'dict',
    'to': 'AUTO',
    'typoResult': 'false',
    'version': '2.1'
}
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(youdaofanyiurl, data)
html = response.read().decode('utf-8')
print(html)

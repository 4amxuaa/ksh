
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding:utf-8
from bottle import Jinja2Template
from bottle import request, route, run, template,view,static_file,response,Response,json_dumps,jinja2_template
import os
import urllib
import requests
import json
import requests
# import requests.packages.urllib3.util.ssl_
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'
import sys


 
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    # reload(sys)
    sys.setdefaultencoding(default_encoding)

@route('/wxyy')
def wxyy():
    # username = request.forms.get('username')
    # password = request.forms.get('password')
    # print(username,password)
    reqbasicInfo = urllib.parse.unquote(request.query_string)
    # print(reqbasicInfo)
    print(request.query_string)
    data = request.query_string  # http://127.0.0.1:8888/wxyy?&wx=
    data = reqbasicInfo.split("=")[1]
    r = wxyy(data)
    print(r)
    return {"data":r}

@route('/ts1')
def index():
    return template('vant听书主页')

@route('/<path:path>')
def path(path):
    cookies = request.cookies
    key = request.get_cookie('key', secret = 'usafe')
    basicInfo = urllib.parse.unquote(request.url)

    currentPath=os.path.dirname(os.path.realpath(__file__)) #获取当前路径
    print(path)
    print(currentPath+"/"+path)
    data = static_file(currentPath+"/"+path,root=currentPath,charset="utf-8") #,download=True
    return data 

@route('/ts')
def index():
    return template('vant听书')
@route('/wx')
def index():
    return template('文心')

run(host='127.0.0.1', port=8888, debug=True)

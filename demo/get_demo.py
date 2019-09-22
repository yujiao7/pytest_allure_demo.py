#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/10'
# 自动化get 方式
# 先创建一个项目，建一个Demo包，在建一个模块
# 在Terminal输入命令pip install requests导入requests 包
# 无数据
from urllib import request

import requests


def no_paramters():
    r = requests.get("http://qa.yansl.com:8080/prefrenceArea/listAll")
    print(r.text)
    # text代表响应正文中的所有数据，并且是字符串形式
    print("应正文中的数据（字符串格式):"+ r.text)
    print("应正文中的数据（字典格式):", r.json())
    print("响应正文中的数据（二进制格式）:",r.content)#没有进行转换
    print("应正文中的数据（响应状态码):", r.status_code)
    print("响应头中的数据:",r.headers)
    print("请求行（请求方法):", r.request.method)
    print("请求头）url):", r.request.url)
    print("请求头:",r.request.headers)
    print("请求正文:",r.request.body)

# 键值对
def jian_zhi_dui():
    para = {
        "name":"admin",
        "pagesize":5,
        "pageNum":1
    }
    # params作用就是传键值对类型数据，位置在url后边，参数是一个字典类型变量
    r = requests.get("http://qa.yansl.com:8080/admin/list",params=para)
    print(r.text)
# 数据在uri里边
def in_uri():
   r=requests.get("http://qa.yansl.com:8080/admin/role/{}".format(4))# format 取{}里面的变量
   print(r.text)

# 下载文件
def download_file():
        data = {
            "pwd": "yj123456",
            "userName": "yj123456"
        }

        r = requests.post("http://api.yansl.com:8084/login", json=data)
        print(r.text)
        token = r.json()["data"]["token"]
        header = {'token': token, 'charset': 'utf-8'}
        r = requests.get("http://api.yansl.com:8084/product/downRepertoryTemplate",headers=header)
        conetent = r.content
        with open('sss.xls','wb')as f :
            f.write(conetent)



if __name__ == '__main__':
    # no_paramters()
    # # jian_zhi_dui()
    # in_uri()
    download_file()
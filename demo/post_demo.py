#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/10'
# 自动化post 方式 requests框架
import os

import requests

d = {} # 转换成字典放在最上面

def no_data():
   pass
# josn

def json_data():
    data ={
  "password": "123456",#后台里面的格式复制加上值
  "username": "admin"
}
    r = requests.post("http://qa.yansl.com:8080/admin/login",json = data)
    print(r.text)
    r_dict = r.json()
    tokenHead = r_dict["data"]["tokenHead"]
    token = r_dict["data"]["token"]
    # print(tokenHead) #直接取值
    # print(token)     #直接取值
    d ["tokenHead"]=tokenHead# 转换成字典模式
    d["token"] = token # 转换成字典模式

# 无参
def no_data():
    header = {"Authorization": d["tokenHead"] + d["token"]}
    # headers 请求头中天健内容，参数类型 字典
    r = requests.post("http://qa.yansl.com:8080/admin/logout",headers = header)
    print(r.text)
# 键值对
def jian_zhi_dui():
    da = {"adminId":86,"roleIds":[1,2,3,4]}
    # post 请求传键值对数据，用data，参数类型dict
    r = requests.post("http://qa.yansl.com:8080/admin/role/update",data = da)
    print(r.text)
# 上传文件
def upload_file():
    data ={
  "pwd": "yj123456",
  "userName": "yj123456"
}

    r =requests.post("http://api.yansl.com:8084/login",json = data)
    print(r.text)
    token = r.json()["data"]["token"]
    file ={'file':open(("sku.xls"),'rb')}
    print(file)
    header = {'token':token,'charset':'utf-8'}
    rl = requests.post("http://api.yansl.com:8084/product/uploaProdRepertory",files =file,headers = header)
    print(rl.text)



if __name__ == '__main__':
    # json_data()
    # no_data()
    # jian_zhi_dui()
    upload_file()
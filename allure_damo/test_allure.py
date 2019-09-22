#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/11'

import allure
# 改用例名字
@allure.feature("模块名")  #一级包名
@allure.story("接口名1")  # 二级接口名模块名
@allure.title("我有一个小毛驴1")  #三级用例名
def test_demo1():
    print('我是damo1')
    allure.step("断言")            # 增加断言
    allure.attach("实际结果:1,预期结果:1",'断言',allure.attachment_type.TEXT)   # 断言显示内容
    assert 1==1


@allure.feature("模块名")
@allure.story("接口名2")
@allure.title("我有一个小毛驴2")
def test_demo2():
    print('我是damo1')
    allure.step("断言")
    allure.attach("实际结果:2,预期结果:2", '断言', allure.attachment_type.TEXT)
    assert 1==1

# 给测试用例设计优先级  blocker, critical, normal, minor, trivial
@allure.severity("blocker")  # 修改优先级
@allure.testcase("http://www.baidu.com",'百度一下')  # 关联用例连接,后面跟'自己改的名字'作用是为了能点击连接查看
@allure.issue("http://www.baidu.com",'百度') # 关联bug单 域名连接 后可改'自己想改的名字' 作用是为了能点击连接查看
@allure.feature("模块名")
@allure.story("接口名3")
@allure.title("我有一个小毛驴3")
def test_demo3():
    print('我是damo1')
    assert 1==1
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/10'
# 先输入命令pip install pytest导入
import pytest
 # @标记名
# 所有的用例
# 类
# 生效范围
# 执行脚本文件时候

# 谁用放在（）括号里面



@pytest.mark.wuhou
def test_dazhaohu_hello(kai_gua):# 第一种括号里面
    print("hello")


@pytest.mark.wuhou
def test_dazhaohu_nihao(kai_gua):
    print(kai_gua)

    print('你好')


@pytest.mark.zaijian
def test_dazhaohu_bye():
    print("再见")


@pytest.mark.zaijian
def test_dazhaohu_libie():
    print("离别")



# parametrize参数
data = [["张三","小明"],["赵四","小芳"],["王五","小王"],["赵六","小赵"],["钱七","小钱"],["王八","小王八"],["高九","小高"]]
@pytest.mark.parametrize("name,name2",data)
@pytest.mark.zaijian
def test_dazhaohu_libie(name,name2):
    print("你好：",name,"我是:",name2)







# 断言
data = [["张三","小明"],["赵四","小芳"],["王五","小王"],["赵六","小赵"],["钱七","小钱"],["王八","小王八"],["高九","小高"]]
@pytest.mark.parametrize("name,name2",data)
@pytest.mark.zaijian
def test_dazhaohu_libie(name,name2):
    assert "赵四"== name   # 断言
    print("你好：",name,"我是:",name2)
# 美化测试报告 输入命令pip install allure-pytest导第三方包 安装一个插件D:\software\allure-2.4.1\bin路径在电脑里面属性配置环境里面找到环境变量里面路径后面加上;加路径；结束，然后去cmd里面输入命令allure
# pip install allure-pytest==2.7.0
# allure generate ./report/xml -o ./report/html --clean
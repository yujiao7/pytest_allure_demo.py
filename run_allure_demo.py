#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/11'
import pytest
# 先执行方法然后调用这方法最后输入命令allure generate ./report/xml -o ./report/html --clean



pytest.main(["allure_damo/",'-v','--alluredir','report/xml']) # 显示测试用例报告
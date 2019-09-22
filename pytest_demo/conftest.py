#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/11'
# 作用范围：conftest.py文件所在包及其子包
# fixture函数，如果存在多个同名的遵循就近原则
import pytest


@pytest.fixture(scope="session")
def kai_gua():
    print("我是外挂，我先执行11")
    # return ("老是开挂")
    yield    # 后置步骤
    print("我是外挂，我先执行22")
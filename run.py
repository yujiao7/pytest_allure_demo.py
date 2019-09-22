#!/usr/bin/env python
# -*- coding: utf-8 -*-

#__title__ = ''
#__author__ = 'xuepl'
#__mtime__ = '2019/9/10'
# pytest main 方法放在新的模块里面
import pytest
# 需要执行哪个包和模块输入包名和模块名，加上-v 然后在直接查看
pytest.main(['-v'"pytest_medo/test_demo.py"])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from r3py import r3temp


def test_noerror():
    try:
        r3temp.printInfo()
    except:
        assert False

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from r3py import r3temp


def test_noerror():
    try:
        r3temp.printInfo()
    except:
        assert False


def test_existing():
    api = r3temp.r3temp()
    try:
        api.getTemp()
        api.getTempByName('Temp@CX')
    except:
        assert False
        return
    assert True


def test_nonexisting():
    api = r3temp.r3temp()
    try:
        api.getTempByName('Temp@NonExist')
    except:
        assert True
        return
    assert False

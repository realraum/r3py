#!/usr/bin/env python
# -*- coding: utf-8 -*-

from r3py import temp


def test_noerror():
    try:
        temp.printInfo()
    except:
        assert False


def test_existing():
    api = temp()
    try:
        api.getTemp()
        api.getTempByName('Temp@CX')
    except:
        assert False
        return
    assert True


def test_nonexisting():
    api = temp()
    try:
        api.getTempByName('Temp@NonExist')
    except:
        assert True
        return
    assert False

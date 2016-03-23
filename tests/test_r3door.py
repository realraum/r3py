#!/usr/bin/env python
# -*- coding: utf-8 -*-

from r3py import r3door


def test_noerror():
    try:
        r3door.printInfo()
    except:
        assert False


def test_existing():
    api = r3door()
    try:
        api.getDoorstatus()
    except:
        assert False
        return
    assert True


def test_nonexisting():
    api = r3door()
    try:
        api.getStatusByName('NonexistingLock')
    except:
        assert True
        return
    assert False

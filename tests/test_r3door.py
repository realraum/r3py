#!/usr/bin/env python
# -*- coding: utf-8 -*-

from r3py import door


def test_noerror():
    try:
        door.printInfo()
    except:
        assert False


def test_existing():
    api = door()
    try:
        api.getDoorstatus()
    except:
        assert False
        return
    assert True


def test_nonexisting():
    api = door()
    try:
        api.getStatusByName('NonexistingLock')
    except:
        assert True
        return
    assert False

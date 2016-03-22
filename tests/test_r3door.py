#!/usr/bin/env python
# -*- coding: utf-8 -*-

from r3py import r3door


def test_noexception():
    try:
        r3door.printInfo()
    except:
        assert False

#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class CDataType:

    def __init__(self):
        self.id = None
        self.name = None
        self.description = None


class CProtocol:

    def __init__(self):
        self.id = None
        self.name = None

        self.pull = False
        self.push = False
        self.get = False
        self.put = False


class CDataProvider:

    ROLE_SOURCE = 1
    ROLE_SINK = 2
    SOLE_TWOWAY = 3

    def __init__(self):
        self.id = None

#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

from c_common import CDataType


class BuiltInDataTypes:

    @staticmethod
    def getDataTypeDict():
        ret = dict()

        if True:
            dt = CDataType()
            dt.id = "file"
            dt.name = "File"
            ret[dt.id] = dt

        if True:
            dt = CDataType()
            dt.id = "directory"
            dt.name = "Directory"
            ret[dt.id] = dt




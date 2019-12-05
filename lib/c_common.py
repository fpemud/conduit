#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import re
import uuid
from OpenSSL import crypto
from c_util import CUtil
from c_param import CConst


class CDataInterfaceFile:
    pass




class CProtocolException(Exception):
    pass


class CBusinessException(Exception):
    pass


class CPluginApi:

    ProtocolException = CProtocolException
    BusinessException = CBusinessException

    def __init__(self, param, sessObj):
        self.param = param
        self.sessObj = sessObj

        self.procDir = os.path.join(self.sessObj.sysObj.getMntDir(), "proc")
        self.sysDir = os.path.join(self.sessObj.sysObj.getMntDir(), "sys")
        self.devDir = os.path.join(self.sessObj.sysObj.getMntDir(), "dev")
        self.runDir = os.path.join(self.sessObj.sysObj.getMntDir(), "run")
        self.tmpDir = os.path.join(self.sessObj.sysObj.getMntDir(), "tmp")
        self.varDir = os.path.join(self.sessObj.sysObj.getMntDir(), "var")
        self.varTmpDir = os.path.join(self.varDir, "tmp")
        self.homeDirForRoot = os.path.join(self.sessObj.sysObj.getMntDir(), "root")
        self.lostFoundDir = os.path.join(self.sessObj.sysObj.getMntDir(), "lost+found")

        self.hasHomeDirForRoot = False
        self.hasVarDir = False

    def getUuid(self):
        return self.sessObj.sysObj.getUuid()

    def getCpuArch(self):
        return self.sessObj.sysObj.getClientInfo().cpu_arch

    def getIpAddress(self):
        return self.sessObj.sslSock.getpeername()[0]

    def getCertificate(self):
        return self.sessObj.sslSock.get_peer_certificate()

    def getPublicKey(self):
        return self.sessObj.sysObj.pubkey

    def getRootDir(self):
        return self.sessObj.sysObj.getMntDir()


class CPluginManager:

    @staticmethod
    def getPluginNameList():
        ret = []
        for fn in os.listdir(CConst.pluginsDir):
            if fn == "__pycache__":
                continue
            if os.path.isdir(fn):
                ret.append(fn)
            else:
                ret.append(fn.replace(".py", ""))
        return ret

    @staticmethod
    def loadPluginObject(pluginName, param, ctrlSession):
        exec("import plugins.%s" % (pluginName))
        return eval("plugins.%s.PluginObject(param, CPluginApi(param, ctrlSession))" % (pluginName))


class CClientInfo:

    def __init__(self):
        self.hostname = None
        self.cpu_arch = None
        self.capacity = None            # how much harddisk this client occupy
        self.ssh_pubkey = None

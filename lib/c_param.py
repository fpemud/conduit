#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os


class CConst:

    user = "root"              # fixme
    group = "root"             # fixme

    libDir = "/usr/lib64/conduit-daemon"
    pluginsDir = os.path.join(libDir, "plugins")
    runDir = "/run/conduit-daemon"
    varDir = "/var/lib/conduit-daemon"

    keySize = 1024

    avahiSupport = True


class CParam:

    def __init__(self):
        self.cacheDir = "/var/cache/conduit-daemon"
        self.logDir = "/var/log/conduit-daemon"
        self.tmpDir = None

        self.certFile = os.path.join(CConst.varDir, "cert.pem")
        self.privkeyFile = os.path.join(CConst.varDir, "privkey.pem")

        self.ctrlPort = 2201
        self.pidFile = os.path.join(CConst.runDir, "conduit-daemon.pid")
        self.logLevel = None

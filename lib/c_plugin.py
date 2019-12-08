#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import sys
import imp
import libxml2
import threading
from gi.repository import GLib


class CPluginManager:

    def __init__(self, param):
        self.param = param

    def loadPlugins(self):
        ret = []
        for pluginName in os.listdir(CConst.pluginsDir):
            pluginPath = os.path.join(self.param.pluginsDir, pluginName)
            self._load(pluginName, pluginPath)

    def _load(self, name, path):
        # get metadata.xml file
        metadata_file = os.path.join(path, "metadata.xml")
        if not os.path.exists(metadata_file):
            raise Exception("plugin %s has no metadata.xml" % (name))
        if not os.path.isfile(metadata_file):
            raise Exception("metadata.xml for plugin %s is not a file" % (name))
        if not os.access(metadata_file, os.R_OK):
            raise Exception("metadata.xml for plugin %s is invalid" % (name))

        # check metadata.xml file content
        # FIXME
        tree = libxml2.parseFile(metadata_file)
        # if True:
        #     dtd = libxml2.parseDTD(None, constants.PATH_PLUGIN_DTD_FILE)
        #     ctxt = libxml2.newValidCtxt()
        #     messages = []
        #     ctxt.setValidityErrorHandler(lambda item, msgs: msgs.append(item), None, messages)
        #     if tree.validateDtd(ctxt, dtd) != 1:
        #         msg = ""
        #         for i in messages:
        #             msg += i
        #         raise exceptions.IncorrectPluginMetaFile(metadata_file, msg)

        # get data from metadata.xml file
        root = tree.getRootElement()

        # create CDataProvider objects
        for child in root.xpathEval(".//data-provider"):
            obj = CDataProvider(self.param, self, path, child)
            assert obj.id not in self.param.dataProviderDict
            self.param.dataProviderDict[obj.id] = obj

        # create CDataProviderFactory objects
        for child in root.xpathEval(".//data-provider-factory"):
            obj = CDataProviderFactory(self.param, self, path, child)
            assert obj.id not in self.param.dataProviderFactoryDict
            self.param.dataProviderFactoryDict[obj.id] = obj

        # create CDataType objects
        for child in root.xpathEval(".//data-type"):
            obj = CDataType(self.param, self, path, child)
            assert obj.id not in self.param.dataTypeDict
            self.param.dataTypeDict[obj.id] = obj

        # create CProtocolType objects
        # FIXME: should only consider direct child
        for child in root.xpathEval(".//protocol"):
            obj = CProtocolType(self.param, self, path, child)
            assert obj.id not in self.param.dataTypeDict
            self.param.dataTypeDict[obj.id] = obj






        # record plugin id
        self.param.pluginList.append(root.prop("id"))


class CDataProvider:

    def __init__(self, param, pluginDir, rootElem):
        self.id = rootElem.prop("id")

        # data directory
        self.dataDir = rootElem.xpathEval(".//data-directory")[0].getContent()
        self.dataDir = os.path.join(param.cacheDir, self.dataDir)

        # updater
        self.updaterObj = None
        self.schedExpr = None
        self.useWorkerProc = None
        if True:
            elem = rootElem.xpathEval(".//updater")[0]

            self.schedExpr = elem.xpathEval(".//cron-expression")[0].getContent()
            # FIXME: add check

            ret = elem.xpathEval(".//runtime")
            if len(ret) > 0:
                self.runtime = ret[0].getContent()
                # FIXME: add check
            else:
                self.runtime = "glib-mainloop"

            filename = os.path.join(pluginDir, elem.xpathEval(".//filename")[0].getContent())
            classname = elem.xpathEval(".//classname")[0].getContent()
            while True:
                if self.runtime == "glib-mainloop":
                    try:
                        f = open(filename)
                        m = imp.load_module(filename[:-3], f, filename, ('.py', 'r', imp.PY_SOURCE))
                        plugin_class = getattr(m, classname)
                    except:
                        raise Exception("syntax error")
                    self.updaterObj = plugin_class()
                    break

                if self.runtime == "thread":
                    self.updaterObj = _UpdaterObjProxyRuntimeThread(filename, classname)
                    break

                if self.runtime == "process":
                    self.updaterObj = _UpdaterObjProxyRuntimeProcess(param, filename, classname)
                    break

                assert False

        # advertiser
        self.advertiseProtocolList = []
        for child in rootElem.xpathEval(".//advertiser")[0].xpathEval(".//protocol"):
            self.advertiseProtocolList.append(child.getContent())


# data-provider ###############################################################

class TemplateDataProvider:

    def activate(self, api):
        assert False

    def deactivate(self):
        assert False

    def get_data_init_param(self, data_type):
        # optional
        assert False

    def get_protocol_init_param(self, protocol):
        # optional
        assert False


# data-provider-factory #######################################################

class TemplateDataProviderFactory:

    def activate(self, api):
        assert False

    def deactivate(self):
        assert False


# data ########################################################################

class TemplateData:

    def __init__(self, init_param, api):
        assert False

    def get_checksum(self):
        assert False

    def get_delta(self, checksum):
        assert False

    def merge(self, delta):
        assert False


# protocol ####################################################################

class TemplateProtocol:

    def __init__(self, init_param, api):
        assert False

    def start_accept_push_reject_conflict(self):
        # returns protocol_data
        assert False

    def start_accept_push_report_conflict(self):
        # returns protocol_data
        assert False

    def start_accept_push_overwrite_conflict(self):
        # returns protocol_data
        assert False

    def stop_accept_push(self):
        assert False

    def start_accept_pull_reject_conflict(self):
        # returns protocol_data
        assert False

    def start_accept_pull_report_conflict(self):
        # returns protocol_data
        assert False

    def start_accept_pull_overwrite_conflict(self):
        # returns protocol_data
        assert False

    def stop_accept_pull(self):
        assert False

    def push_reject_conflict(self, peer_protocol_data):
        assert False

    def push_report_conflict(self, peer_protocol_data):
        assert False

    def push_overwrite_conflict(self, peer_protocol_data):
        assert False

    def pull_reject_conflict(self, peer_protocol_data):
        assert False

    def pull_report_conflict(self, peer_protocol_data):
        assert False

    def pull_overwrite_conflict(self, peer_protocol_data):
        assert False

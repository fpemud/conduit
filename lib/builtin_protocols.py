#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

from c_common import CProtocol


class BuiltInProtocols:

    @staticmethod
    def getProtocolDict():
        ret = dict()

        if True:
            p = CProtocol()
            p.id = "conduit-file"
            p.pull_reject_conflict = True
            p.pull_report_conflict = True
            p.pull_overwrite_conflict = True
            p.push_reject_conflict = True
            p.push_report_conflict = True
            p.push_overwrite_conflict = True
            p.pullerDict["conduit-file-puller"] = _FilePuller
            p.pulleeDict["conduit-file-pullee"] = _FilePullee
            p.localPullerDict["conduit-file-local-puller"] = _FileLocalPuller
            p.pusherDict["conduit-file-pusher"] = _FilePusher
            p.pusheeDict["conduit-file-pushee"] = _FilePushee
            p.localPusherDict["conduit-file-local-pusher"] = _FileLocalPusher
            ret[p.id] = p

        if True:
            p = CProtocol()
            p.id = "conduit-directory"
            p.pull_reject_conflict = True
            p.pull_report_conflict = True
            p.pull_overwrite_conflict = True
            p.push_reject_conflict = True
            p.push_report_conflict = True
            p.push_overwrite_conflict = True
            p.pullerDict["conduit-directory-puller"] = _FilePuller
            p.pulleeDict["conduit-directory-pullee"] = _FilePullee
            p.localPullerDict["conduit-directory-local-puller"] = _FileLocalPuller
            p.pusherDict["conduit-directory-pusher"] = _FilePusher
            p.pusheeDict["conduit-directory-pushee"] = _FilePushee
            p.localPusherDict["conduit-directory-local-pusher"] = _FileLocalPusher
            ret[p.id] = p


class _FilePuller:
    pass


class _FilePullee:
    pass


class _FileLocalPuller:
    pass


class _FilePusher:
    pass


class _FilePushee:
    pass


class _FileLocalPusher:
    pass













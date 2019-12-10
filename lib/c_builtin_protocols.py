#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

class InBandProtocolFile:

    @staticmethod
    def get_id():
        return "file"

    @staticmethod
    def get_properties():
        return {
            "can-push": True,
            "can-be-pushed-reject-conflict": True,
            "can-be-pushed-report-conflict": True,
            "can-be-pushed-overwrite-conflict": True,
            "can-pull-reject-conflict": True,
            "can-pull-report-conflict": True,
            "can-pull-overwrite-conflict": True,
            "can-be-pulled": True,
        }

    def __init__(self, init_param, api):
        self._path = init_param
        self._api = api

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

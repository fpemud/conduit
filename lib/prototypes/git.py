#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class ConduitProtocolGit:

    @staticmethod
    def get_id():
        return "git"

    @staticmethod
    def get_properties():
        return {
            "can-push": True,
            "can-be-pushed-reject-conflict": True,
            "can-be-pushed-report-conflict": False,
            "can-be-pushed-overwrite-conflict": False,      # FIXME
            "can-pull-reject-conflict": True,
            "can-pull-report-conflict": True,
            "can-pull-overwrite-conflict": True,
            "can-be-pulled": True,
        }

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

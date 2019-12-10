#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class ConduitGitPushClient:

    def __init__(self, api):
        assert False

    def push_reject_conflict(self, peer_protocol_data):
        assert False

    def push_report_conflict(self, peer_protocol_data):
        assert False

    def push_overwrite_conflict(self, peer_protocol_data):
        assert False


class ConduitGitPushServer:

    def __init__(self, api):
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


class ConduitGitPullClient:

    def __init__(self, api):
        assert False

    def pull_reject_conflict(self, peer_protocol_data):
        assert False

    def pull_report_conflict(self, peer_protocol_data):
        assert False

    def pull_overwrite_conflict(self, peer_protocol_data):
        assert False


class ConduitGitPullServer:

    def __init__(self, api):
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


class GitPushClient:

    def __init__(self, api):
        assert False

    def push_reject_conflict(self, peer_protocol_data):
        assert False

    def push_report_conflict(self, peer_protocol_data):
        assert False

    def push_overwrite_conflict(self, peer_protocol_data):
        assert False


class GitPushServer:

    def __init__(self, api):
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


class GitPullClient:

    def __init__(self, api):
        assert False

    def pull_reject_conflict(self, peer_protocol_data):
        assert False

    def pull_report_conflict(self, peer_protocol_data):
        assert False

    def pull_overwrite_conflict(self, peer_protocol_data):
        assert False


class GitPullServer:

    def __init__(self, api):
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

#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class TemplateDataProvider:

    def activate(self, api):
        assert False

    def deactivate(self):
        assert False

    def get_data_init_param(self, data_type):
        assert False

    def get_protocol_init_param(self, protocol):
        assert False

    # FIXME
    def register_auto_push(self):
        assert False

    # FIXME
    def unregister_auto_push(self):
        assert False

    # FIXME
    def is_auto_push_registered(self):
        assert False


class TemplateDataProviderApi:

    def get_tmp_dir(self):
        assert False

    def get_log_dir(self):
        assert False


class TemplateDataProviderFactory:

    def activate(self, api):
        assert False

    def deactivate(self):
        assert False


class TemplateDataProviderFactoryApi:

    def get_tmp_dir(self):
        assert False

    def get_log_dir(self):
        assert False

    def data_provider_added(self, data_provider):
        assert False

    def data_provider_removed(self, data_provider):
        # FIXME, param should be id or obj?
        assert False


class TemplateData:

    def __init__(self, init_param, api):
        assert False

    def get_checksum(self):
        # optional
        assert False

    def get_delta(self, checksum):
        # optional
        assert False

    def merge(self, delta):
        # optional
        assert False


class TemplateDataApi:

    def get_tmp_dir(self):
        assert False

    def get_log_dir(self):
        assert False


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


class TemplateProtocolApi:

    def get_tmp_dir(self):
        assert False

    def get_log_dir(self):
        assert False

    def get_peer_ip(self):
        assert False




























# common interface for Data
class Data:

    @read
    def get_mtime(self):
        pass

    @write
    def set_mtime(self):
        pass

# interface for Data if the data is text string
class DataText:
        pass

# interface for Data if the data is binary blob
class DataBinary:
        pass

# interface for Data if the data is a file
class DataFile:
        pass

# interface for Data if the data is a directory
class DataDirectory:
        pass

# interface for Data if the data is 
class DataContainer:
    pass

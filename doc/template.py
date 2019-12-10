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


class TemplateDataMergable:

    def __init__(self, init_param, api):
        assert False

    def get_checksum(self):
        assert False

    def get_delta(self, checksum):
        assert False

    def merge(self, delta):
        assert False


class TemplateDataCopyable:

    def __init__(self, init_param, api):
        assert False

    def read(self):
        assert False

    def write(self, data):
        assert False


class TemplateDataApi:

    def get_tmp_dir(self):
        assert False

    def get_log_dir(self):
        assert False


class TemplatePushClient:

    def push_reject_conflict(self, api):
        assert False

    def push_report_conflict(self, api):
        assert False

    def push_overwrite_conflict(self, api):
        assert False


class TemplatePushServer:

    def start_accept_push_reject_conflict(self, api):
        # returns protocol_data
        assert False

    def start_accept_push_report_conflict(self, api):
        # returns protocol_data
        assert False

    def start_accept_push_overwrite_conflict(self, api):
        # returns protocol_data
        assert False

    def stop_accept_push(self):
        assert False


class TemplatePullClient:

    def pull_reject_conflict(self, api):
        assert False

    def pull_report_conflict(self, api):
        assert False

    def pull_overwrite_conflict(self, api):
        assert False


class TemplatePullServer:

    def start_accept_pull_reject_conflict(self, api):
        # returns protocol_data
        assert False

    def start_accept_pull_report_conflict(self, api):
        # returns protocol_data
        assert False

    def start_accept_pull_overwrite_conflict(self, api):
        # returns protocol_data
        assert False

    def stop_accept_pull(self):
        assert False


class TemplateProtocolApi:

    def get_init_data(self):
        assert False

    def get_tmp_dir(self):
        assert False

    def get_log_dir(self):
        assert False

    def get_peer_ip(self):
        assert False

    def accept_conflict(self):
        assert False



class TemplatePushClientApi(TemplateProtocolApi):
    
    def get_server_ip(self):
        assert False

    def get_server_data(self):
        assert False


class TemplatePushServerApi(TemplateProtocolApi):

    def get_client_ip(self):
        assert False


class TemplatePullClientApi(TemplateProtocolApi):

    def get_server_ip(self):
        assert False

    def get_server_data(self):
        assert False


class TemplatePullServerApi(TemplateProtocolApi):

    def get_client_ip(self):
        assert False


class TemplateDataType:

    def check(self, param):
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




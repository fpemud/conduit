#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class OutOfBandProtocolRsync:

    @staticmethod
    def get_id():
        return "rsync"

    @staticmethod
    def get_properties():
        return {
            "can-push": True,
            "can-be-pushed-reject-conflict": False,
            "can-be-pushed-report-conflict": False,
            "can-be-pushed-overwrite-conflict": True,
            "can-pull-reject-conflict": False,
            "can-pull-report-conflict": False,
            "can-pull-overwrite-conflict": True,
            "can-be-pulled": True,
        }

    def __init__(self, init_param, api):
        self._path = init_param
        self._api = api

        self._cfgFile = os.path.join(self._api.get_tmp_dir(), "rsync.cfg")
        self._lockFile = os.path.join(self._api.get_tmp_dir(), "rsync.lock")
        self._logFile = os.path.join(self._api.get_log_dir(), "rsync.log")
        self._port = None
        self._proc = None

    def start_accept_push_reject_conflict(self):
        return self._acceptPush()

    def start_accept_push_report_conflict(self):
        return self._acceptPush()

    def start_accept_push_overwrite_conflict(self):
        return self._acceptPush()

    def stop_accept_push(self):
        assert False

    def start_accept_pull_reject_conflict(self):
        return self._acceptPull()

    def start_accept_pull_report_conflict(self):
        return self._acceptPull()

    def start_accept_pull_overwrite_conflict(self):
        return self._acceptPull()

    def stop_accept_pull(self):
        if self._proc is not None:
            self._proc.terminate()
            self._proc.wait()
            self._proc = None
        self._port = None

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

    def _acceptPull(self):
        port = _Util.getFreeTcpPort()

        buf = ""
        buf += "lock file = %s\n" % (self._lockFile)
        buf += "log file = %s\n" % (self._logFile)
        buf += "\n"
        buf += "port = %s\n" % (self._port)
        buf += "max connections = 1\n"
        buf += "timeout = 600\n"
        buf += "\n"
        buf += "use chroot = yes\n"
        buf += "uid = root\n"
        buf += "gid = root\n"
        buf += "\n"
        buf += "[data]\n"
        buf += "path = %s\n" % (self._path)
        buf += "read only = yes\n"
        with open(self._cfgFile, "w") as f:
            f.write(buf)

        cmd = ""
        cmd += "/usr/bin/rsync --daemon --no-detach --config=\"%s\"" % (self._cfgFile)
        proc = subprocess.Popen(cmd, shell=True, universal_newlines=True)

        self._proc = proc
        self._port = port
        return self._port



    def pull_overwrite_conflict(self, peer_protocol_data):
        port = peer_protocol_data

        source = "rsync://%s:%d/overlay" % (self._api.get_peer_ip(), port)
        cmd = "/usr/bin/rsync -a -z --delete %s %s >%s 2>&1" % (source, self._overlayDir, self._logFile)
        _Util.shellCall(cmd)

        source = "rsync://%s:%d/distfiles" % (self._api.get_peer_ip(), port)
        cmd = "/usr/bin/rsync -a -z --delete %s %s >%s 2>&1" % (source, self._distfilesDir, self._logFile)
        _Util.shellCall(cmd)

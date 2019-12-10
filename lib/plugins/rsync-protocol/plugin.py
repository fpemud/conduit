#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-

import os
import time
import subprocess


class ConduitRsyncPushClient:

    def push_overwrite_conflict(self, api):
        localDir = api.get_init_data()
        logFile = os.path.join(api.get_log_dir(), "rsync-push.log")
        port, dstName = api.get_server_data()

        url = "rsync://%s:%d/%s" % (api.get_server_ip(), port, dstName)
        cmd = "/usr/bin/rsync -a -z --delete %s %s >%s 2>&1" % (localDir, url, logFile)
        _Util.shellCall(cmd)


class ConduitRsyncPushServer:

    def __init__(self):
        self._api = None
        self._path = None
        self._cfgFile = None
        self._lockFile = None
        self._logFile = None
        self._proc = None

    def start_accept_push_overwrite_conflict(self, api):
        try:
            path = self._api.get_init_data()
            port = _Util.getFreeTcpPort()

            self._api = api
            self._cfgFile = os.path.join(self._api.get_tmp_dir(), "rsync.cfg")
            self._lockFile = os.path.join(self._api.get_tmp_dir(), "rsync.lock")
            self._logFile = os.path.join(self._api.get_log_dir(), "rsync.log")

            buf = ""
            buf += "lock file = %s\n" % (self._lockFile)
            buf += "log file = %s\n" % (self._logFile)
            buf += "\n"
            buf += "port = %s\n" % (port)
            buf += "max connections = 1\n"
            buf += "timeout = 600\n"
            buf += "\n"
            buf += "use chroot = yes\n"
            buf += "uid = root\n"
            buf += "gid = root\n"
            buf += "\n"
            buf += "[data]\n"
            buf += "path = %s\n" % (path)
            buf += "read only = no\n"
            with open(self._cfgFile, "w") as f:
                f.write(buf)

            cmd = "/usr/bin/rsync --daemon --no-detach --config=\"%s\"" % (self._cfgFile)
            self._proc = subprocess.Popen(cmd, shell=True, universal_newlines=True)

            return (port, "data")
        except:
            self.stop_accept_push()
            raise

    def stop_accept_push(self):
        if self._proc is not None:
            self._proc.terminate()
            self._proc.wait()
            self._proc = None
        self._logFile = None
        if self._lockFile is not None:
            os.unlink(self._lockFile)
            self._lockFile = None
        if self._cfgFile is not None:
            os.unlink(self._cfgFile)
            self._cfgFile = None
        self._api = None


class ConduitRsyncPullClient:

    def pull_overwrite_conflict(self, api):
        localDir = api.get_init_data()
        logFile = os.path.join(api.get_log_dir(), "rsync-pull.log")
        port, srcName = api.get_server_data()

        url = "rsync://%s:%d/%s" % (api.get_server_ip(), port, srcName)
        cmd = "/usr/bin/rsync -a -z --delete %s %s >%s 2>&1" % (url, localDir, logFile)
        _Util.shellCall(cmd)


class ConduitRsyncPullServer:

    def __init__(self):
        self._api = None
        self._path = None
        self._cfgFile = None
        self._lockFile = None
        self._logFile = None
        self._proc = None

    def start_accept_pull_overwrite_conflict(self, api):
        try:
            path = self._api.get_init_data()
            port = _Util.getFreeTcpPort()

            self._api = api
            self._cfgFile = os.path.join(self._api.get_tmp_dir(), "rsync.cfg")
            self._lockFile = os.path.join(self._api.get_tmp_dir(), "rsync.lock")
            self._logFile = os.path.join(self._api.get_log_dir(), "rsync.log")

            buf = ""
            buf += "lock file = %s\n" % (self._lockFile)
            buf += "log file = %s\n" % (self._logFile)
            buf += "\n"
            buf += "port = %s\n" % (port)
            buf += "max connections = 1\n"
            buf += "timeout = 600\n"
            buf += "\n"
            buf += "use chroot = yes\n"
            buf += "uid = root\n"
            buf += "gid = root\n"
            buf += "\n"
            buf += "[data]\n"
            buf += "path = %s\n" % (path)
            buf += "read only = yes\n"
            with open(self._cfgFile, "w") as f:
                f.write(buf)

            cmd = "/usr/bin/rsync --daemon --no-detach --config=\"%s\"" % (self._cfgFile)
            self._proc = subprocess.Popen(cmd, shell=True, universal_newlines=True)

            return (port, "data")
        except:
            self.stop_accept_pull()
            raise

    def stop_accept_pull(self):
        if self._proc is not None:
            self._proc.terminate()
            self._proc.wait()
            self._proc = None
        self._logFile = None
        if self._lockFile is not None:
            os.unlink(self._lockFile)
            self._lockFile = None
        if self._cfgFile is not None:
            os.unlink(self._cfgFile)
            self._cfgFile = None
        self._api = None


class RsyncPushClient:

    def push_reject_conflict(self, api):
        assert False

    def push_report_conflict(self, api):
        assert False

    def push_overwrite_conflict(self, api):
        assert False


class RsyncPushServer:

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


class RsyncPullClient:

    def __init__(self, api):
        assert False

    def pull_reject_conflict(self, peer_protocol_data):
        assert False

    def pull_report_conflict(self, peer_protocol_data):
        assert False

    def pull_overwrite_conflict(self, peer_protocol_data):
        assert False


class RsyncPullServer:

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








class _Util:

    @staticmethod
    def getFreeTcpPort(start_port=10000, end_port=65536):
        for port in range(start_port, end_port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.bind((('', port)))
                return port
            except socket.error:
                continue
            finally:
                s.close()
        raise Exception("No valid tcp port in [%d,%d]." % (start_port, end_port))

    @staticmethod
    def shellCall(cmd):
        # call command with shell to execute backstage job
        # scenarios are the same as FmUtil.cmdCall

        ret = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                             shell=True, universal_newlines=True)
        if ret.returncode > 128:
            # for scenario 1, caller's signal handler has the oppotunity to get executed during sleep
            time.sleep(1.0)
        if ret.returncode != 0:
            ret.check_returncode()
        return ret.stdout.rstrip()
































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

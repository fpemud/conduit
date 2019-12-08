#!/usr/bin/python3
# -*- coding: utf-8; tab-width: 4; indent-tabs-mode: t -*-


class DataProvider:

    def activate(self, api):
        pass

    def deactivate(self):
        pass


class Protocol:

    def __init__(self, init_param, api):
        self._overlayDir = "/var/lib/portage/laymanfiles/fpemud-private"
        self._distfilesDir = "/var/lib/portage/distfiles-private"

        self._api = api

        self._cfgFile = os.path.join(self._api.get_tmp_dir(), "rsync.cfg")
        self._lockFile = os.path.join(self._api.get_tmp_dir(), "rsync.lock")
        self._logFile = os.path.join(self._api.get_log_dir(), "rsync.log")
        self._port = None
        self._proc = None

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

    def pull_overwrite_conflict(self, peer_protocol_data):
        port = peer_protocol_data

        source = "rsync://%s:%d/overlay" % (self._api.get_peer_ip(), port)
        cmd = "/usr/bin/rsync -a -z --delete %s %s >%s 2>&1" % (source, self._overlayDir, self._logFile)
        _Util.shellCall(cmd)

        source = "rsync://%s:%d/distfiles" % (self._api.get_peer_ip(), port)
        cmd = "/usr/bin/rsync -a -z --delete %s %s >%s 2>&1" % (source, self._distfilesDir, self._logFile)
        _Util.shellCall(cmd)

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
        buf += "[overlay]\n"
        buf += "path = %s\n" % (self._overlayDir)
        buf += "read only = yes\n"
        buf += "\n"
        buf += "[distfiles]\n"
        buf += "path = %s\n" % (self._distfilesDir)
        buf += "read only = yes\n"
        with open(self._cfgFile, "w") as f:
            f.write(buf)

        cmd = ""
        cmd += "/usr/bin/rsync --daemon --no-detach --config=\"%s\"" % (self._cfgFile)
        proc = subprocess.Popen(cmd, shell=True, universal_newlines=True)

        self._proc = proc
        self._port = port
        return self._port


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



# def _acceptPull(self):
#     try:
#         self._port = _Util.getFreeTcpPort()
#         self._logfile = "/dev/null"
#         cmd = "/usr/bin/git daemon --export-all --port=%d %s 2>%s" % (self._port, self._overlayDir, self._logfile)
#         self._proc = subprocess.Popen(cmd, shell=True, universal_newlines=True)
#         return self._port
#     except:
#         self._stopAcceptPull()
#         raise

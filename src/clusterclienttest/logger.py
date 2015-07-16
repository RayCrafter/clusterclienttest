import logging
import os
import socket

import graypy


class PBSFilter(logging.Filter):
    def __init__(self):
        self.jobid = os.environ.get('PBS_JOBID', -1)
        self.logname = os.environ.get('PBS_O_LOGNAME')
        self.jobname = os.environ.get('PBS_JOBNAME')
        self.queue = os.environ.get('PBS_QUEUE')

    def filter(self, record):
        record.jobid = self.jobid
        record.submitter = self.logname
        record.jobname = self.jobname
        record.queue = self.queue
        record.fqdn = socket.getfqdn()
        return True


def setup_logger(name, host, port):
    log = logging.getLogger(name)
    handler = graypy.GELFHandler(host, port)
    log.addHandler(handler)
    log.addFilter(PBSFilter())
    return log

#!/usr/bin/env python

import logging
import re
import subprocess
import sys
import time

RETRIES = 20
LOG = logging.getLogger(__name__)


def get_job_state(job_id):
    res = {}
    for i in range(RETRIES):
        try:
            sacct_res = subprocess.check_output(["sacct", "-Pbnj", job_id])
            res = {s.split("|")[0]: s.split("|")[1] for s in sacct_res.decode().strip().splitlines()}
            break
        except subprocess.CalledProcessError as cpe:
            LOG.error("sacct process error")
            LOG.error(cpe)
        except IndexError as ie:
            LOG.error(ie)

        # scontrol as a backup if sacct for some reason fails
        try:
            scontrol_res = subprocess.check_output(["scontrol", "-o", "show", "job", job_id])
            m = re.search(r"JobState=(\w+)", scontrol_res.decode())
            if m is None:
                LOG.error("failed to parse scontrol output")
                if i >= RETRIES - 1:
                    print("failed")
                    sys.exit(0)
                else:
                    time.sleep(1)
                    continue
            res = {job_id: m.group(1)}
            break
        except subprocess.CalledProcessError as cpe:
            LOG.error("scontrol process error")
            LOG.error(cpe)
            if i >= RETRIES - 1:
                print("failed")
                sys.exit(0)
            else:
                time.sleep(1)

    return res.get(job_id, "")


def get_job_status(state):
    if state in ("CONFIGURING", "COMPLETING", "PENDING", "RUNNING", "SUSPENDED"):
        return "running"
    elif state == "COMPLETED":
        return "success"
    elif state in ("BOOT_FAIL", "DEADLINE", "FAILED", "NODE_FAIL", "OUT_OF_MEMORY", "PREEMPTED", "TIMEOUT"):
        return "failed"
    elif state.startswith("CANCELLED"):
        return "failed"
    else:
        return "running"


if __name__ == '__main__':
    job_id = sys.argv[1]
    job_state = get_job_state(job_id)
    job_status = get_job_status(job_state)
    print(job_status)

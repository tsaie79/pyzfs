from fireworks import FiretaskBase, explicit_serialize

from atomate.utils.utils import env_chk, get_logger, logger

from pyzfs.common.wfc.vasploader import VaspWavefunctionLoader
from pyzfs.zfs.main import ZFSCalculation

import subprocess
import os


@explicit_serialize
class RunPyzfs(FiretaskBase):
    """
    run pyzfs
    zfs_cmd:
        srun -n 2048 -c 2 python /home/tug03990/site-packages/pyzfs/examples/VASP/run.py > out (cori)
        mpiexec -n 20 pyzfs --wfcfmt vasp > out (owls, efrc)
    """
    required_params = ["pyzfs_cmd"]

    def run_task(self, fw_spec):
        cmd = env_chk(self["pyzfs_cmd"], fw_spec)
        logger.info("Running command: {}".format(cmd))
        return_code = subprocess.call([cmd], shell=True)
        logger.info("Command {} finished running with returncode: {}".format(cmd, return_code))



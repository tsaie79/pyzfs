from pyzfs.workflows.firetasks import RunPyzfs

from fireworks import Firework

from atomate.common.firetasks.glue_tasks import PassCalcLocs
from atomate.vasp.firetasks.glue_tasks import CopyVaspOutputs

class PyzfsFW(Firework):
    def __init__(
            self,
            parents=None,
            structure=None,
            name="pyzfs",
            prev_calc_dir=None,
            pyzfs_cmd=">>pyzfs_cmd<<",
            **kwargs
    ):
        fw_name = "{}-{}".format(
            structure.composition.reduced_formula if structure else "unknown", name
        )

        t = []

        if prev_calc_dir:
            t.append(
                CopyVaspOutputs(
                    calc_dir=prev_calc_dir,
                    additional_files=["WAVECAR"],
                    contcar_to_poscar=True,
                )
            )
        elif parents:
            t.append(
                CopyVaspOutputs(
                    calc_loc=True,
                    additional_files=["WAVECAR"],
                    contcar_to_poscar=True,
                )
            )
        else:
            raise ValueError("Must specify structure or previous calculation")

        t.append(RunPyzfs(pyzfs_cmd=pyzfs_cmd))
        t.append(PassCalcLocs())
        super(PyzfsFW, self).__init__(t, parents=parents, name=fw_name, **kwargs)
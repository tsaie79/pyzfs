from pyzfs.common.wfc.vasploader import VaspWavefunctionLoader
from pyzfs.zfs.main import ZFSCalculation
wfcloader = VaspWavefunctionLoader()  # Construct wavefunction loader
zfscalc = ZFSCalculation(wfcloader=wfcloader)  # Set up ZFS calculation
zfscalc.solve()  # Perform ZFS calculation
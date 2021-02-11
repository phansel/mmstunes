#/bin/python3
# Paul Hansel 2019 

import numpy as np
import sounddevice as sd

import cdflib

cdfname = "mms1_edp_brst_l2_dce_20160809085854_v2.2.0.cdf"

x = cdflib.CDF("./" + cdfname)

data = x.varget("mms1_edp_dce_par_epar_brst_l2")

tdata = np.transpose(data)[1]

data = tdata * 1/np.max(np.abs(tdata))

print("The maximum electric field observed was " +
            str(np.max(np.abs(tdata))) + " mV/m.")

spacecraft = '1'
year = '2016'
month = '08'
datatype = "epar"
day = '09'

fs = 16384
#fs = 44100

sd.play(data, fs, blocking=True)

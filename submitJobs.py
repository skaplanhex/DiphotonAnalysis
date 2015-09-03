#! /usr/bin/env python

import glob
import os

# jdls = glob.glob("*.jdl")
# only run Ms=2500 GeV jobs
# jdls = glob.glob("*ADDdiPhoton*.jdl")
# jdls = glob.glob("*6500*.jdl") + glob.glob("*7000*.jdl")
# jdls = glob.glob("*Neg*jdl")
# jdls = glob.glob("ADDdiPhoton_sherpa_13TeV_KK1_NED4*jdl")
jdls = ("ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS2500_MGG2000-ms.jdl","ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG200-750.jdl","ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG2000-ms.jdl","ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS7000_MGG2000-ms.jdl")
for jdl in jdls:
    if jdl == "condor.jdl":
        continue
    else:
        print "Now submitting %s"%jdl
        os.system("condor_submit %s"%jdl)
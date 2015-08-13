#! /usr/bin/env python

import glob
import os

# jdls = glob.glob("*.jdl")
# only run Ms=2500 GeV jobs
jdls = glob.glob("*ADDdiPhoton*.jdl")
# jdls = glob.glob("*6500*.jdl") + glob.glob("*7000*.jdl")
# jdls = glob.glob("*Neg*jdl")

for jdl in jdls:
    if jdl == "condor.jdl":
        continue
    else:
        print "Now submitting %s"%jdl
        os.system("condor_submit %s"%jdl)
#! /usr/bin/env python

import glob
import os

jdls = glob.glob("*.jdl")

for jdl in jdls:
    if jdl == "condor.jdl":
        continue
    else:
        print "Now submitting %s"%jdl
        os.system("condor_submit %s"%jdl)
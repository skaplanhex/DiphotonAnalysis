#! /bin/bash

export SCRAM_ARCH=slc6_amd64_gcc481
source /cvmfs/cms.cern.ch/cmsset_default.sh

cd /uscms_data/d3/skaplan/diphotons/p8sherpacomparison/CMSSW_7_2_4/src/Analyzers/DiphotonAnalyzer
eval `scramv1 runtime -sh`

cd ${_CONDOR_SCRATCH_DIR}
cmsRun diphotonanalyzer_cfg.py inputCfi=$1 maxEvents=-1 outfilename=$2 leadingPtCut=80. subleadingPtCut=80.

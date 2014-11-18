#! /bin/bash

export SCRAM_ARCH=slc5_amd64_gcc462
source /uscmst1/prod/sw/cms/shrc prod

cd /uscms_data/d3/skaplan/diphotons/CMSSW_7_1_1/src
eval `scramv1 runtime -sh`
cd ${_CONDOR_SCRATCH_DIR}

let lambdat=($1+1)*500
echo lambdaT: $lambdat

cmsRun exampleanalyzer_cfg.py maxEvents=-1 outfilename=plots_LambdaTstudy_LambdaT$lambdat.root infilename=diphoton_signal_LambdaT$1.root

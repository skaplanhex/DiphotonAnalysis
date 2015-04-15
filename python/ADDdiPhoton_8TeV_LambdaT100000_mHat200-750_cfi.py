import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_10_1_GAC.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_1_1_HB3.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_2_1_vpR.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_3_1_2dH.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_4_1_zfR.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_5_1_gpf.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_6_1_Qd3.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_7_1_p6m.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_8_1_3tk.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/LambdaT100000_mHat200-750/ADDGravitonToGG_13TeV_pythia8_GEN_9_1_rhD.root',
    )

)

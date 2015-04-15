import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_10_1_BhA.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_1_1_zkx.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_2_1_gTB.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_3_1_2Kb.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_4_1_Rox.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_5_1_rgc.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_6_1_r5Y.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_7_1_KAG.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_8_1_gME.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg750-2000_Ms4000/sherpaevents_9_1_h1L.root',
    )

)

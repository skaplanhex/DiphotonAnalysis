import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_10_1_ckT.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_1_1_GAL.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_2_1_KCL.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_3_1_gAv.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_4_1_jka.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_5_1_d6W.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_6_1_yWj.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_7_1_U9A.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_8_1_zlp.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms3000/sherpaevents_9_1_MuK.root',
    )

)

import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_10_1_Lzk.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_1_1_eqG.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_2_1_mYA.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_3_1_4cb.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_4_1_SMW.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_5_1_JlA.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_6_1_tAp.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_7_1_1IX.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_8_1_Cxn.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms3000/sherpaevents_9_1_LEc.root',
    )

)

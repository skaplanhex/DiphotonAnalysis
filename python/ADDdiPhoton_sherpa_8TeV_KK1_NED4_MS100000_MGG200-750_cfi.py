import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_10_1_NB3.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_1_1_n6V.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_2_1_BP8.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_3_1_RYZ.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_4_1_goj.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_5_1_ucl.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_6_1_Zwe.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_7_1_g9c.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_8_1_rr2.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms100000/sherpaevents_9_1_XiN.root',
    )

)

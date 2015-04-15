import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_10_1_hkz.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_1_1_Q6N.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_2_1_c40.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_3_1_ly5.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_4_1_BuF.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_5_1_eAv.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_6_1_gwl.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_7_1_PEj.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_8_1_WC4.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms100000/sherpaevents_9_1_Zqp.root',
    )

)

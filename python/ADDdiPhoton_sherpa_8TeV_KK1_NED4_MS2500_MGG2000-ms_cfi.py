import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_10_1_uWK.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_1_1_rBa.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_2_1_62i.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_3_1_ahR.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_4_1_run.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_5_1_cRs.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_6_1_pIO.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_7_1_hhQ.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_8_1_bge.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms2500/sherpaevents_9_1_YbY.root',
    )

)

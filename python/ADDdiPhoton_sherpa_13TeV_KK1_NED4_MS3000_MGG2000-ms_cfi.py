import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_10_1_8kg.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_1_1_Xp4.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_2_1_pXp.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_3_1_EqO.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_4_1_9Pd.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_5_1_n0G.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_6_1_fMS.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_7_1_Nyz.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_8_1_tzT.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg2000-ms_Ms3000/sherpaevents_9_1_gUp.root',
    )

)

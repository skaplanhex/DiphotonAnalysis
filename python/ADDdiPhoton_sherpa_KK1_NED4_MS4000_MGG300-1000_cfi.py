import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_10_1_mbV.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_1_1_CHV.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_2_1_Hb6.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_3_1_aPx.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_4_1_HzV.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_5_1_ul5.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_6_1_Erh.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_7_1_lsf.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_8_1_y3X.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms4000/sherpaevents_9_1_GeE.root',
    )

)

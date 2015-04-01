import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_10_1_EV3.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_1_1_VN3.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_2_1_TPa.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_3_1_6oL.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_4_1_Qpq.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_5_1_TiO.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_6_1_tAp.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_7_1_TJs.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_8_1_dFp.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms3000/sherpaevents_9_1_PD8.root',
    )

)

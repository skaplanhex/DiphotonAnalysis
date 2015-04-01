import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_10_1_xOR.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_1_1_opK.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_2_1_9AQ.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_3_1_ve7.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_4_1_6F7.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_5_1_9vc.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_6_1_PQi.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_7_1_eNX.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_8_1_vuu.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms3000/sherpaevents_9_1_0AS.root',
    )

)

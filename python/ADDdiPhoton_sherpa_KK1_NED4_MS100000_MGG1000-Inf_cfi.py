import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_10_1_r8n.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_1_1_Qt5.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_2_1_cZi.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_3_1_BMo.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_4_1_met.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_5_1_RLA.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_6_1_WB5.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_7_1_LM6.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_8_1_yNU.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms100000/sherpaevents_9_1_a68.root',
    )

)

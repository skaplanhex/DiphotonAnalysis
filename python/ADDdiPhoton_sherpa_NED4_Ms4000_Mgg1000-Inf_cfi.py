import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_10_1_zpT.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_1_1_3or.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_2_1_AGt.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_3_1_bDJ.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_4_1_3HM.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_5_1_VD4.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_6_1_zeF.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_7_1_lq7.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_8_1_wqe.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms4000/sherpaevents_9_1_y5I.root',
    )

)

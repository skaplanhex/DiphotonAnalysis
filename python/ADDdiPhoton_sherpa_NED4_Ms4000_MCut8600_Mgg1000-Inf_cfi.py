import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_10_1_rTD.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_1_1_03M.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_2_1_Iyq.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_3_1_1wd.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_4_1_Ils.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_5_1_HCB.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_6_1_1uu.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_7_1_Xiv.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_8_1_v13.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms4000/sherpaevents_9_1_SsL.root',
    )

)

import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_10_1_ghR.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_1_1_b7v.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_2_1_CLp.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_3_1_vTB.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_4_1_97F.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_5_1_vbP.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_6_1_Wnp.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_7_1_vP0.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_8_1_wQX.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms100000/sherpaevents_9_1_ngg.root',
    )

)

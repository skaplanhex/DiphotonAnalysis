import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_10_1_Ddk.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_1_1_rh9.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_2_1_6UL.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_3_1_gZq.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_4_1_WVs.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_5_1_mJE.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_6_1_EBB.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_7_1_I0K.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_8_1_7id.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa/mgg1000-Inf_ms2000/sherpaevents_9_1_QEK.root',
    )

)

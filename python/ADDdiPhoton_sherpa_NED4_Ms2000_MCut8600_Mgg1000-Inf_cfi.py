import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_10_1_fno.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_1_1_pPZ.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_2_1_j7r.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_3_1_gl9.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_4_1_kyg.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_5_1_twJ.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_6_1_IxF.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_7_1_ECV.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_8_1_hzL.root',
        '/store/user/skaplan/noreplica/diphoton/sherpa2/mgg1000-Inf_ms2000/sherpaevents_9_1_KUh.root',
    )

)

import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_10_1_4Mf.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_1_1_BbE.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_2_1_f6c.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_3_1_u4y.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_4_1_m6R.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_5_1_xQj.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_6_1_PKY.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_7_1_ESw.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_8_1_x63.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms3500/sherpaevents_9_1_xUp.root',
    )

)

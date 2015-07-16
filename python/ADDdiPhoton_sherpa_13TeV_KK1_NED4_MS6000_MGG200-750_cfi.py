import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_10_1_O4V.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_1_1_rUW.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_2_1_k0r.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_3_1_k22.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_4_2_wS9.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_5_1_hK0.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_6_1_3Ku.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_7_1_WXp.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_8_1_4Pl.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6000/sherpaevents_9_1_uV2.root',
    )

)

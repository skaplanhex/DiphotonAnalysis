import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_10_1_UET.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_1_1_RWO.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_2_1_e4U.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_3_1_j2h.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_4_1_px2.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_5_1_y53.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_6_1_qTz.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_7_1_ky1.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_8_1_7xS.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms5000/sherpaevents_9_1_l2f.root',
    )

)

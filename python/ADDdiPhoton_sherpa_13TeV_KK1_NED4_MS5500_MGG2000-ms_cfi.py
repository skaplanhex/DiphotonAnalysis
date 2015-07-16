import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_10_1_3Bv.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_1_1_GY3.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_2_1_GcN.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_3_1_RhQ.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_4_1_Wnh.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_5_1_LWr.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_6_1_yRQ.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_7_1_Lqk.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_8_1_EOx.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms5500/sherpaevents_9_1_oyy.root',
    )

)

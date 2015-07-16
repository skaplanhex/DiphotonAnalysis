import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_10_1_M5O.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_1_1_6Et.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_2_1_6Be.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_3_1_kSu.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_4_1_s1t.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_5_1_Kd0.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_6_1_x1z.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_7_1_Vd9.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_8_1_EeX.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms100000/sherpaevents_9_1_sXU.root',
    )

)

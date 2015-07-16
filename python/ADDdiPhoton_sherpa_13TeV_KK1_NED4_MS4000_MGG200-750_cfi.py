import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_10_1_okb.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_1_1_JYU.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_2_1_Se8.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_3_1_Rpn.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_4_1_btx.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_5_1_z7a.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_6_1_Tk5.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_7_1_A13.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_8_1_Cq5.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms4000/sherpaevents_9_1_40E.root',
    )

)

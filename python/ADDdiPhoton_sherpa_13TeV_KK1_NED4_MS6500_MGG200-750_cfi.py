import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_10_1_2Z8.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_1_1_pub.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_2_1_HDD.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_3_1_Slh.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_4_1_Fnk.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_5_1_uAN.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_6_1_oN4.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_7_1_0Oq.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_8_1_dfD.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg200-750_Ms6500/sherpaevents_9_1_0IJ.root',
    )

)

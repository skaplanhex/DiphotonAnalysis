import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_10_1_wmn.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_1_1_CI1.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_2_1_U3x.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_3_1_54q.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_4_1_7ZG.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_5_1_IsY.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_6_1_kSA.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_7_1_Urq.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_8_1_5Mn.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms2500/sherpaevents_9_1_zJJ.root',
    )

)

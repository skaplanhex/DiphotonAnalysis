import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_10_1_08V.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_1_1_S5H.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_2_1_Pc8.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_3_1_IEj.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_4_1_deG.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_5_1_VmD.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_6_1_mYP.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_7_1_88u.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_8_1_9nh.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms7000/sherpaevents_9_1_zuO.root',
    )

)

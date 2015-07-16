import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_10_1_Kji.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_1_1_oTR.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_2_1_A2c.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_3_1_TNY.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_4_1_F6B.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_5_1_L2p.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_6_1_vz3.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_7_1_c3E.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_8_1_w8E.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3000/sherpaevents_9_1_FNA.root',
    )

)

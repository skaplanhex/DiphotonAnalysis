import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_10_1_ad7.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_1_2_Oq5.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_2_1_DJk.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_3_1_qJt.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_4_1_PQV.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_5_1_2IY.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_6_1_lfi.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_7_1_HmF.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_8_2_IZr.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms3500/sherpaevents_9_1_RI7.root',
    )

)

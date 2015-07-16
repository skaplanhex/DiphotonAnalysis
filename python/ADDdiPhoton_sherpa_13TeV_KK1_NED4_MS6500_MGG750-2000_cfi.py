import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_10_1_NCO.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_1_1_DZM.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_2_1_php.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_3_1_u4k.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_4_1_ne3.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_5_1_A9x.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_6_1_bgj.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_7_1_d7Y.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_8_1_Pm8.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg750-2000_Ms6500/sherpaevents_9_1_k6p.root',
    )

)

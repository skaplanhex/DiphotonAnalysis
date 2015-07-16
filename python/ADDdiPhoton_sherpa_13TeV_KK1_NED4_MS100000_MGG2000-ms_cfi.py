import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_10_1_HKN.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_1_1_JFS.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_2_1_6qx.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_3_1_3OU.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_4_1_HRB.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_5_1_rff.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_6_1_jeB.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_7_1_kbQ.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_8_1_zKx.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms100000/sherpaevents_9_1_qE5.root',
    )

)

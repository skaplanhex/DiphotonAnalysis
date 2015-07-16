import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_10_1_aaO.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_1_1_RvD.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_2_1_0qb.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_3_1_Uoa.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_4_1_H4e.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_5_1_Jj7.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_6_1_euo.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_7_1_a0T.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_8_1_4kv.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms4500/sherpaevents_9_1_CrD.root',
    )

)

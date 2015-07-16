import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_10_1_YhD.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_1_1_SQq.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_2_1_K5e.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_3_1_ZGJ.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_4_1_yoI.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_5_1_ZtX.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_6_1_0GZ.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_7_1_0l3.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_8_1_xOr.root',
        '/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/mgg2000-ms_Ms6000/sherpaevents_9_1_Fay.root',
    )

)

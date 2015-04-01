import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_10_1_1dZ.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_1_1_VAc.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_2_1_PDp.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_3_1_JqE.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_4_1_6vj.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_5_1_Dos.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_6_1_a21.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_7_1_XRn.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_8_1_Xzw.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg1000-Inf_Ms5000/sherpaevents_9_1_bcx.root',
    )

)

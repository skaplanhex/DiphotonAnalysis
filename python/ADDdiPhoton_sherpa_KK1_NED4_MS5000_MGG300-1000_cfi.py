import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_10_1_DGc.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_1_1_ttm.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_2_1_4TF.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_3_1_DaP.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_4_1_r4F.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_5_1_d0b.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_6_1_H2Q.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_7_1_RQ6.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_8_1_lbj.root',
        '/store/user/skaplan/noreplica/sherpaevents/mgg300-1000_Ms5000/sherpaevents_9_1_EXU.root',
    )

)

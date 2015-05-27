import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_10_1_B6s.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_1_1_OWG.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_2_1_kXu.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_3_1_kIr.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_4_1_wM9.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_5_1_h9X.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_6_1_tOC.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_7_1_iXd.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_8_1_6E5.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms2500/sherpaevents_9_1_nBL.root',
    )

)

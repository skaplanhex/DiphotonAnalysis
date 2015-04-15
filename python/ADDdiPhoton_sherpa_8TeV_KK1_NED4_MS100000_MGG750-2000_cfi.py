import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_10_1_lZp.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_1_1_rCq.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_2_1_qCw.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_3_1_ggG.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_4_1_PhI.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_5_1_Ng2.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_6_1_qHp.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_7_1_Amr.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_8_1_VM9.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms100000/sherpaevents_9_1_6ZG.root',
    )

)

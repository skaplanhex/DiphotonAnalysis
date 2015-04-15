import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_10_1_yjk.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_1_1_2rb.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_2_1_w8X.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_3_1_y06.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_4_1_lT5.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_5_1_0XG.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_6_1_7yj.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_7_1_XLS.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_8_1_7lR.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms4000/sherpaevents_9_1_hsK.root',
    )

)

import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_10_1_Y7r.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_1_1_scS.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_2_1_6Tt.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_3_1_m2S.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_4_1_JUX.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_5_1_0Yh.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_6_1_P4O.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_7_1_3Nr.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_8_1_xIc.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms3000/sherpaevents_9_1_axh.root',
    )

)

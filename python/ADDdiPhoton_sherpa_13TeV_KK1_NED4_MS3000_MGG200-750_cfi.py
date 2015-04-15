import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_10_1_6n0.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_1_1_u56.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_2_1_YHy.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_3_1_beD.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_4_1_m63.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_5_1_BB1.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_6_1_o2Z.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_7_1_pG5.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_8_1_AXB.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/13TeV/mgg200-750_Ms3000/sherpaevents_9_1_Oa9.root',
    )

)

import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_10_1_hxZ.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_1_1_xaF.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_2_1_2HE.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_3_1_qGi.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_4_1_JGm.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_5_1_bYG.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_6_1_W9C.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_7_1_Wm2.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_8_1_BoQ.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg200-750_Ms2500/sherpaevents_9_1_G5k.root',
    )

)

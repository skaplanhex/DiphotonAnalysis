import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_10_1_h4e.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_1_1_Av8.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_2_1_Q4y.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_3_1_htH.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_4_1_pfq.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_5_1_TBw.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_6_1_JqZ.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_7_1_Wy8.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_8_1_Ed9.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg750-2000_Ms4000/sherpaevents_9_1_ADW.root',
    )

)

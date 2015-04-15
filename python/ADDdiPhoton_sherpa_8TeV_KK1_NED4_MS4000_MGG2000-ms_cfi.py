import FWCore.ParameterSet.Config as cms

source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_10_1_kA1.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_1_1_Nab.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_2_1_tCJ.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_3_1_Ewy.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_4_1_GKL.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_5_1_RmA.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_6_1_oXa.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_7_1_M0n.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_8_1_7Vs.root',
        '/store/user/skaplan/noreplica/p8sherpacomparison/sherpa/8TeV/mgg2000-ms_Ms4000/sherpaevents_9_1_FhX.root',
    )

)

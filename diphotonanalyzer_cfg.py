from FWCore.ParameterSet.VarParsing import VarParsing

options = VarParsing ('python')

options.register('inputCfi',
                 "DUMMY",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "input cfi file name"
)
options.register('infilename',
                 "DUMMY",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "input file name"
)

options.register('outfilename',
                 "plots.root",
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.string,
                 "output file name"
)
options.register('leptonMode',
                  False,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "whether or not to look at leptons instead of photons"
)
options.register('leadingPtCut',
                 60.,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "leading photon pt cut"
)
options.register('subleadingPtCut',
                 60.,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.float,
                 "subleading photon pt cut"
)
options.register('makeTree',
                False,
                VarParsing.multiplicity.singleton,
                VarParsing.varType.bool,
                "whether or not to include a tree in the output file")
options.register('useAOD',
                True,
                VarParsing.multiplicity.singleton,
                VarParsing.varType.bool,
                "running over AOD?")
## 'maxEvents' is already registered by the Framework, changing default value
options.setDefault('maxEvents', -1)

options.parseArguments()

import FWCore.ParameterSet.Config as cms

process = cms.Process("USER")

process.load("FWCore.MessageService.MessageLogger_cfi")

#how many events to process.  -1 means all of them
process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(options.maxEvents) )

if (options.inputCfi != "DUMMY"):
  process.load( "Analyzers.DiphotonAnalyzer.%s"%(options.inputCfi) )
  # process.source = cms.Source("PoolSource",
  #   fileNames = cms.untracked.vstring(
  #     # 'file:/uscms_data/d3/skaplan/diphotons/CMSSW_7_1_1/src/%s'%(options.infilename)
  #     '/store/user/skaplan/noreplica/diphoton/%s'%(options.infilename)
  #   )
elif (options.infilename != "DUMMY"):
  process.source = cms.Source("PoolSource",
      fileNames = cms.untracked.vstring( "file:%s"%(options.infilename) )
  )
  
else:
  process.source = cms.Source("PoolSource",
      # replace 'myfile.root' with the source file you want to use
      fileNames = cms.untracked.vstring(
         # 'file:/uscms_data/d3/skaplan/diphotons/CMSSW_7_1_1/src/ADD_M-1200_13TeV_N4_MD2000.root'
         #'file:/uscms_data/d3/skaplan/diphotons/CMSSW_7_1_1/src/ADD_M-1200_13TeV_N2_MD2000_RUN2.root'
         'root://cmsxrootd.fnal.gov//store/mc/RunIIFall15DR76/GGJets_M-1000To2000_Pt-50_13TeV-sherpa/AODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/10000/0814B407-5ED8-E511-9DAB-0CC47A78A414.root'
         # 'root://cmsxrootd.fnal.gov//store/mc/RunIIFall15MiniAODv2/GGJets_M-4000To6000_Pt-50_13TeV-sherpa/MINIAODSIM/PU25nsData2015v1_76X_mcRun2_asymptotic_v12-v1/40000/30EA0953-91D8-E511-8F65-0025907B4F64.root'
         # '/store/mc/Summer12_DR53X/RSGravitonToGG_kMpl01_M_1000_Tune4C_8TeV_pythia8_cff/AODSIM/PU_S10_START53_V19-v1/20000/3A864739-9D0A-E311-A554-002590A80DF0.root',
         # '/store/mc/Summer12_DR53X/RSGravitonToGG_kMpl01_M_1000_Tune4C_8TeV_pythia8_cff/AODSIM/PU_S10_START53_V19-v1/20000/3CD38A6B-C30B-E311-A996-002590A37122.root',
         # '/store/mc/Summer12_DR53X/RSGravitonToGG_kMpl01_M_1000_Tune4C_8TeV_pythia8_cff/AODSIM/PU_S10_START53_V19-v1/20000/4495277D-500B-E311-A29B-001E6739811F.root',
         # '/store/mc/Summer12_DR53X/RSGravitonToGG_kMpl01_M_1000_Tune4C_8TeV_pythia8_cff/AODSIM/PU_S10_START53_V19-v1/20000/5C65E29A-9F0A-E311-B205-002590A8882A.root'
         # '/store/mc/Summer12_DR53X/VBF_HToGG_M-120_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/7813CDA6-77FA-E111-9141-002618943974.root',
         # '/store/mc/Summer12_DR53X/VBF_HToGG_M-120_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/8CACA74D-7BFA-E111-9F30-0030486792A8.root',
         # '/store/mc/Summer12_DR53X/VBF_HToGG_M-120_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/A6CC388D-93FA-E111-A168-0018F3D09688.root',
         # '/store/mc/Summer12_DR53X/VBF_HToGG_M-120_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/B67396FE-76FA-E111-8487-002618943811.root',
         # '/store/mc/Summer12_DR53X/VBF_HToGG_M-120_8TeV-powheg-pythia6/AODSIM/PU_S10_START53_V7A-v1/0000/BC8A8AF2-76FA-E111-A24C-00261894390B.root',
      )
  )

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

#this lets cmsRun know we want TFile output (histograms, TGraphs, etc.)
process.TFileService = cms.Service("TFileService",
      fileName = cms.string(options.outfilename)
)

useAOD = options.useAOD
st = "AOD"
particleCollection = "genParticles"
if not useAOD:
  st = "MiniAOD"
  particleCollection = "prunedGenParticles"

print "#######################"
print "# Running over %s"%st
print "#######################"
#add the example analyzer to the process object
process.analyze = cms.EDAnalyzer('DiphotonAnalyzer',
	#particles is a variable representing an InputTag (a descriptor of a certain object in the event, in this case, the genParticles).  The InputTag desired can be found by doing an edmDumpEventContent on one of the files in the dataset to see all the objects in the event.  Then, choose whatever you want to use.
	particles = cms.InputTag(particleCollection),
  leptonMode = cms.bool(options.leptonMode),
  leadingPtCut = cms.double(options.leadingPtCut),
  subleadingPtCut = cms.double(options.subleadingPtCut),
  makeTree = cms.bool(options.makeTree),
  eventSource = cms.string(options.inputCfi),
  useAOD = cms.bool(useAOD)
)

#the path tells cmsRun which modules to be run in which order. In our case, we just need to run the analyzer
process.p = cms.Path(process.analyze)

import os

for lt in (3000,4000,100000):
    for p in ("200-750","750-2000","2000-lt"):
            # if lt == 2000 and p == "500-Inf":
            #     continue
        folder="LambdaT%i_mHat%s/"%(lt,p)
        # folder = "pTHat%s/"%p
        # eospath = "/eos/uscms/store/user/skaplan/noreplica/LambdaTStudy/"
        eospath = '/eos/uscms/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/'
        shortpath = "/store/user/skaplan/noreplica/p8sherpacomparison/pythia8/8TeV/"
        fullpath = eospath+folder
        outfiles = os.listdir(fullpath)
        outfilesnew=[]
        for f in outfiles:
            outfilesnew.append("        '"+shortpath + folder + f + "',")
        # fname = "ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi.py"%(lt,p)
        fname = "ADDdiPhoton_8TeV_LambdaT%i_mHat%s_cfi.py"%(lt,p)
        # fname = "ADDdiPhoton_LambdaT%i_pTHat%s_Hewett1_cfi.py"%(lt,p)
        print "Creating %s"%fname
        out = open(fname,'w')
        out.write("import FWCore.ParameterSet.Config as cms\n")
        out.write("\n")
        out.write('source = cms.Source("PoolSource",\n')
        out.write("    fileNames = cms.untracked.vstring(\n")
        for f in outfilesnew:
            out.write(f+"\n")
        out.write("    )\n")
        out.write("\n")
        out.write(")\n")
        out.close()
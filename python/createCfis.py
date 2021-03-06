import os

for lt in (2500,3000,3500,4000,4500,5000,5500,6000,6500,7000):
    for p in ("200-750","750-2000","2000-lt"):
            # if lt == 2000 and p == "500-Inf":
            #     continue
        folder="LambdaT%i_mHat%s/"%(lt,p)
        # folder = "pTHat%s/"%p
        # eospath = "/eos/uscms/store/user/skaplan/noreplica/LambdaTStudy/"
        eospath = '/eos/uscms/store/user/skaplan/noreplica/ADDdiPhoton_negint/Pythia8/'
        shortpath = "/store/user/skaplan/noreplica/ADDdiPhoton_negint/Pythia8/"
        fullpath = eospath+folder
        outfiles = os.listdir(fullpath)
        outfilesnew=[]
        for f in outfiles:
            outfilesnew.append("        '"+shortpath + folder + f + "',")
        # fname = "ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi.py"%(lt,p)
        fname = "ADDdiPhoton_13TeV_LambdaT%i_NegInt_mHat%s_cfi.py"%(lt,p)
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
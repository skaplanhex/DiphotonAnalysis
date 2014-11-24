import os

for lt in ("100K","2000","3000","3500","4000","4500","5000","6000"):
    for p in ("150-500","500-Inf"):
        folder="LambdaT%s_pTHat%s/"%(lt,p)
        eospath = "/eos/uscms/store/user/skaplan/noreplica/LambdaTStudy/"
        shortpath = "/store/user/skaplan/noreplica/LambdaTStudy/"
        fullpath = eospath+folder
        outfiles = os.listdir(fullpath)
        outfilesnew=[]
        for f in outfiles:
            outfilesnew.append("        '"+shortpath + folder + f + "',")
        fname = "ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi.py"%(lt,p)
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
import os

# for lt in ("100K","2000","3000","3500","4000","4500","5000","6000"):
for lt in (3000,4000,5000,100000):
    for p in ("300-1000","1000-Inf"):
            # if lt == 2000 and p == "500-Inf":
            #     continue
        folder="mgg%s_Ms%i/"%(p,lt)
        # folder = "pTHat%s/"%p
        # eospath = "/eos/uscms/store/user/skaplan/noreplica/LambdaTStudy/"
        eospath = '/eos/uscms/store/user/skaplan/noreplica/sherpaevents/'
        shortpath = "/store/user/skaplan/noreplica/sherpaevents/"
        fullpath = eospath+folder
        outfiles = os.listdir(fullpath)
        outfilesnew=[]
        for f in outfiles:
            outfilesnew.append("        '"+shortpath + folder + f + "',")
        # fname = "ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi.py"%(lt,p)
        fname = "ADDdiPhoton_sherpa_KK1_NED4_MS%i_MGG%s_cfi.py"%(lt,p)
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
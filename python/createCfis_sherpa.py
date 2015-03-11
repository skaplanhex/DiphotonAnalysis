import os

for ms in (2000,4000):

    folder="mgg1000-Inf_ms%i/"%(ms)
    # folder = "pTHat%s/"%p
    # eospath = "/eos/uscms/store/user/skaplan/noreplica/LambdaTStudy/"
    eospath = '/eos/uscms/store/user/skaplan/noreplica/diphoton/sherpa2/'
    shortpath = "/store/user/skaplan/noreplica/diphoton/sherpa2/"
    fullpath = eospath+folder
    outfiles = os.listdir(fullpath)
    outfilesnew=[]
    for f in outfiles:
        outfilesnew.append("        '"+shortpath + folder + f + "',")
    # fname = "ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi.py"%(lt,p)
    fname = "ADDdiPhoton_sherpa_NED4_Ms%i_MCut8600_Mgg1000-Inf_cfi.py"%(ms)
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
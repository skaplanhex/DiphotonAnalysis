import os

userDict = {
    "skaplan" : "sherpa",
    "hn99" : "sherpa_morestats"
}

for lt in (2500,3000,3500,4000,4500,5000,5500,6000,6500,7000,100000):
    for p in ("200-750","750-2000","2000-ms"):

        folder = "mgg%s_Ms%i/"%(p,lt)
            
        eospathsk = '/eos/uscms/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/'
        shortpathsk = "/store/user/skaplan/noreplica/ADDdiPhoton/sherpa/"
        fullpathsk = eospathsk+folder

        eospathharan = '/eos/uscms/store/user/hn99/noreplica/ADDdiPhoton/sherpa_morestats/'
        shortpathharan = "/store/user/hn99/noreplica/ADDdiPhoton/sherpa_morestats/"
        fullpathharan = eospathharan+folder
        outfilessk = os.listdir(fullpathsk)
        outfilesharan = os.listdir(fullpathharan)
        print len(outfilessk),len(outfilesharan)
        outfilesnew=[]
        for f in outfilessk:
            outfilesnew.append("        '"+shortpathsk + folder + f + "',")
        for f in outfilesharan:
            outfilesnew.append("        '"+shortpathharan + folder + f + "',")
        # fname = "ADDGravitontoGG_M1200_LambdaT%s_pTHat%s_cfi.py"%(lt,p)
        fname = "ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS%i_MGG%s_cfi.py"%(lt,p)
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
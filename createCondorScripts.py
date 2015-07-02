# need a condor jdl file and shell script for each cfi file

for ms in (2500,3000,4000,100000):
    for m in ("200-750","750-2000","2000-ms"):
        for sqrts in (8,13):
            cfiName = "ADDdiPhoton_sherpa_%iTeV_KK1_NED4_MS%i_MGG%s_cfi"%(sqrts,ms,m)
            # cfiName = "ADDdiPhoton_%iTeV_LambdaT%i_mHat%s_cfi"%(sqrts,ms,m)
            jdlTemplate = open("condorjdltemplate",'r')
            processName = cfiName[:-4]
            print "Now creating " + processName+".jdl"
            jdlOutfile = open(processName+".jdl",'w')
            lines = jdlTemplate.readlines()
            for i,line in enumerate(lines):
                if i==8:
                    temp = line
                    temp = temp.replace("SKFILL",processName)
                    jdlOutfile.write(temp)
                elif i==9:
                    temp = line
                    temp = temp.replace("SKFILL",processName)
                    jdlOutfile.write(temp)
                elif i==10:
                    temp = line
                    temp = temp.replace("SKFILL",processName)
                    jdlOutfile.write(temp)
                elif i==11:
                    temp = line
                    temp = temp.replace("SKFILL1",cfiName)
                    temp = temp.replace("SKFILL2",processName+".root")
                    jdlOutfile.write(temp)
                else:
                    temp=line
                    jdlOutfile.write(temp)
            jdlOutfile.close()
            jdlTemplate.close()

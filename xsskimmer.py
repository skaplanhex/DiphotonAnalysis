o = open('./xsections_lambdaTstudy.txt','w')
for i in range(20):
    f = open('/uscms/home/skaplan/condor/diphoton_signal_LambdaT500x%i.stdout'%i,'r')
    lt = (i+1)*500
    for line in f:
        s = line.split()
        if len(s) < 5:
            continue
        if s[2]=='fbar' and len(s)>16: #found the xs!
            print "XS for LambdaT = %i: %s +- %s"%(lt,s[-3],s[-2])
            o.write("%i %s %s\n"%(lt,s[-3],s[-2]))
            break
    f.close()
o.close()
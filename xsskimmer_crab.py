from numpy import *

def avgError(errors):
    nEntries = 1.0*len(errors)
    numerator = 0.
    for e in errors:
        numerator += e*e
    return sqrt(numerator/nEntries)

out = open('xsections_LambdaTStudy_SecondRun.txt','w')

for lt in (2000,3000,3500,4000,4500,5000,6000,"100K"):
    for pt in ("150-500","500-Inf"):
        xsections=[]
        errors=[]
        baseFolder = "LambdaTStudyJobs/"
        if lt == "100K":
            baseFolder = "LambdaTStudyJobs_Bkg/"
        d="LambdaT%s_pTHat%s/res/"%(str(lt),pt)
        print "Now looking at LambdaT=%s and pTHatRange=%s"%(str(lt),pt)
        print ""
        for jobNum in range(1,21):
            fname=baseFolder+d+"CMSSW_%i.stdout"%jobNum
            f = open(fname,'r')
            for line in f:
                s = line.split()
                if len(s) < 5:
                    continue
                if s[2]=='fbar' and len(s)>16: #found the xs!
                    print "XS for job number %i: %s +- %s"%(jobNum,s[-3],s[-2])
                    xsections.append( float(s[-3]) )
                    errors.append( float(s[-2]) )
                    # o.write("%i %s %s\n"%(lt,s[-3],s[-2]))
                    break
            f.close()
        xsections = array(xsections)
        errors = array(errors)
        mean = xsections.mean()
        err = avgError(errors)
        out.write("%s %s %e %e\n"%(str(lt),pt,mean,err))
        print "Average XS = %e +- %e"%( mean,err )
        print ""

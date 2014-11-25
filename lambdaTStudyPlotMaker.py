print "loading ROOT and numpy..."
from ROOT import *
from numpy import *
print "done."

gROOT.SetBatch()
#this is a constant
xsbkg150=(1.725150e-10)*(1e12)
xsbkg500=(1.636800e-12)*(1e12)
LUMI = 1. #fb**-1

#build cross section dictionaries
f = open('xsections_LambdaTStudy_SecondRun.txt','r')
xsdict150={}
xsdict500={}
for line in f:
    s = line.split()
    lt = s[0]
    if lt == "100K":
        break
    ptBin = s[1]
    if ptBin == "150-500":
        xsdict150[ int( s[0] ) ]= float( s[2] )*(1e12) # convert to fb
    else:
        xsdict500[ int( s[0] ) ]= float( s[2] )*(1e12) # convert to fb
f.close()

#loop over lambdaTs
for lt in (2000,3000,3500,4000,4500,5000,6000):
    # if lt != 2000:
    #     continue

    #background XSs defined above
    xssigplusbkg150 = xsdict150[lt]
    xssigplusbkg500 = xsdict500[lt]

    xssig150 = xssigplusbkg150-xsbkg150
    xssig500 = xssigplusbkg500-xsbkg500
    # if xssig <=0: #not sure how to deal with this yet.
    #     continue

    sigfile150 = "plots_LambdaTStudy_LambdaT%i_pTHat150-500.root"%(lt)
    sigfile500 = "plots_LambdaTStudy_LambdaT%i_pTHat500-Inf.root"%(lt)
    bkgfile150 = "plots_LambdaTStudy_LambdaT100K_pTHat150-500.root"
    bkgfile500 = "plots_LambdaTStudy_LambdaT100K_pTHat500-Inf.root"

    freg150 = TFile(sigfile150,"READ")
    finf150 = TFile(bkgfile150,"READ")
    freg500 = TFile(sigfile500,"READ")
    finf500 = TFile(bkgfile500,"READ")

    hreg150 = freg150.Get("analyze/hggMass")
    hinf150 = finf150.Get("analyze/hggMass")
    hreg500 = freg500.Get("analyze/hggMass")
    hinf500 = finf500.Get("analyze/hggMass")

    hreg150.Sumw2()
    hinf150.Sumw2()
    hreg500.Sumw2()
    hinf500.Sumw2()

    # hreg150.Rebin(2)
    # hinf150.Rebin(2)
    # hreg500.Rebin(2)
    # hinf500.Rebin(2)

    # hregcopy = hreg.Clone()
    # hinfcopy = hinf.Clone()

    # # hsig = xssigbkg*hreg - xsbkg*hinf
    # hsig = hreg.Clone()
    # hsig.Scale(xssigplusbkg)
    # hsig.Add(hinfcopy,-1.*xsbkg)

    # sigbkgint = float( hreg.Integral(0,hreg.GetNbinsX()+1) )
    # bkgint = float( hinf.Integral(0,hinf.GetNbinsX()+1) )

    #luminosity is 1 fb**-1
    NEVENTS=100000.

    hreg150.Scale( (xssigplusbkg150/NEVENTS)*LUMI )
    hinf150.Scale( (xsbkg150/NEVENTS)*LUMI )
    hreg500.Scale( (xssigplusbkg500/NEVENTS)*LUMI )
    hinf500.Scale( (xsbkg500/NEVENTS)*LUMI )

    # hreg150.GetXaxis().SetRangeUser(0,1600)
    # hinf150.GetXaxis().SetRangeUser(0,1600)
    # hreg500.GetXaxis().SetRangeUser(0,1600)
    # hinf500.GetXaxis().SetRangeUser(0,1600)

    hsig150=hreg150.Clone()
    hsig150.Add(hinf150,-1.)
    hsig500=hreg500.Clone()
    hsig500.Add(hinf500,-1.)

    hreg = hreg150.Clone()
    hreg.Add(hreg500,1.)

    hinf = hinf150.Clone()
    hinf.Add(hinf500,1.)

    hsig = hsig150.Clone()
    hsig.Add(hsig500,1.)

    # for h in (hreg,hinf):
    #     h.Scale( 1./h.Integral() )

    c = TCanvas("c","",1000,800)
    c.Divide(2,2)
    pad1 = c.cd(1)
    hreg.SetLineColor(kBlack)
    hinf.SetLineColor(kRed+1)
    hinf.SetLineStyle(4)
    for h in (hreg,hinf):
        h.SetLineWidth(2)
    # hreg.GetYaxis().SetRangeUser(0,1000)
    hreg.Draw()
    hinf.Draw("same")
    # leg = pad1.BuildLegend()
    pad1.SetLogy()

    # # pad1.SetLogy()
    c.cd(2)
    hsig.SetTitle("(#Lambda_{T}=%i) - (#Lambda_{T}=#infty)"%lt)
    hsig.GetYaxis().SetTitle("(#Lambda_{T}=%i) - (#Lambda_{T}=#infty)"%lt)
    # print xssig
    # hsig.Scale(xssig/hsig.Integral()*LUMI)
    # hsig.GetYaxis().SetRangeUser(-0.01,0.01)
    hsig.Draw()
    
    # integral plot of background
    pad3 = c.cd(3)
    # print hinf.Integral()
    hbkgint = hinf.Clone()
    hbkgint.SetName("hbkgint")
    hbkgint.SetTitle("")
    endBin = hinf.GetNbinsX()+1
    for i in range( 1, endBin):
        x = hinf.Integral(i,endBin)
        hbkgint.SetBinContent(i,x)
    pad3.SetLogy()
    hbkgint.Draw()

    c.cd(4)
    hsigint = hsig.Clone()
    hsigint.SetName("hsigint")
    hsigint.SetTitle("")
    endBin = hsig.GetNbinsX()+1
    for i in range( 1, endBin):
        x = hsig.Integral(i,endBin)
        hsigint.SetBinContent(i,x)
    hsigint.Draw()

    c.SaveAs("massplot_LambdaT%i.png"%(lt))
    # freg.Close()
    # finf.Close()
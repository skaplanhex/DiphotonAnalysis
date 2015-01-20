print "loading ROOT and numpy..."
from ROOT import *
from numpy import *
print "done."

gROOT.SetBatch()
gStyle.SetOptStat(0)

#this is a constant
# xsbkg150=(1.725150e-10)*(1e12)
# xsbkg500=(1.636800e-12)*(1e12)
# xsbkg150PP=(1.723e-10)*(1e12)
# xsbkg500PP=(1.630e-12)*(1e12)

LUMI = 1. #fb**-1

#build cross section dictionaries
f = open('xsections_Dileptoncheck.txt','r')
xsdict150={}
xsdict500={}
for line in f:
    s = line.split()
    lt = s[0]
    # if lt == "100K":
    #     break
    ptBin = s[1]
    if ptBin == "150-500":
        xsdict150[ int( s[0] ) ]= float( s[2] )*(1e12) # convert to fb
    else:
        xsdict500[ int( s[0] ) ]= float( s[2] )*(1e12) # convert to fb
f.close()

#just define background xsections as constants
xsbkg150 = xsdict150[100000]
xsbkg500 = xsdict500[100000]

#loop over LambdaTs
for lt in (2000,4000):

    #background XSs defined above
    xssigplusbkg150 = xsdict150[lt]
    xssigplusbkg500 = xsdict500[lt]

    xssig150 = xssigplusbkg150-xsbkg150
    xssig500 = xssigplusbkg500-xsbkg500
    # if xssig <=0: #not sure how to deal with this yet.
    #     continue

    sigfile150 = "dileptonplots_LambdaT%i_pTHat150-500.root"%(lt)
    sigfile500 = "dileptonplots_LambdaT%i_pTHat500-Inf.root"%(lt)
    bkgfile150 = "dileptonplots_LambdaT100000_pTHat150-500.root"
    bkgfile500 = "dileptonplots_LambdaT100000_pTHat500-Inf.root"
    # bkgfile150PP = "Pythia8_SMffbar2GG_pTHat150-500_plots.root"
    # bkgfile500PP = "Pythia8_SMffbar2GG_pTHat500-Inf_plots.root"

    freg150 = TFile(sigfile150,"READ")
    finf150 = TFile(bkgfile150,"READ")
    # finf150PP = TFile(bkgfile150PP,"READ")
    freg500 = TFile(sigfile500,"READ")
    finf500 = TFile(bkgfile500,"READ")
    # finf500PP = TFile(bkgfile500PP,"READ")

    hreg150 = freg150.Get("analyze/hggMass")
    hinf150 = finf150.Get("analyze/hggMass")
    # hinf150PP = finf150PP.Get("analyze/hggMass")
    hreg500 = freg500.Get("analyze/hggMass")
    hinf500 = finf500.Get("analyze/hggMass")
    # hinf500PP = finf500PP.Get("analyze/hggMass")

    hreg150.Sumw2()
    hinf150.Sumw2()
    # hinf150PP.Sumw2()
    hreg500.Sumw2()
    hinf500.Sumw2()
    # hinf500PP.Sumw2()

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
    # hinf150PP.Scale( (xsbkg150PP/NEVENTS)*LUMI )
    hreg500.Scale( (xssigplusbkg500/NEVENTS)*LUMI )
    hinf500.Scale( (xsbkg500/NEVENTS)*LUMI )
    # hinf500PP.Scale( (xsbkg500PP/NEVENTS)*LUMI )

    # hreg150.GetXaxis().SetRangeUser(0,1600)
    # hinf150.GetXaxis().SetRangeUser(0,1600)
    # hreg500.GetXaxis().SetRangeUser(0,1600)
    # hinf500.GetXaxis().SetRangeUser(0,1600)

    hsig150=hreg150.Clone()
    hsig150.Add(hinf150,-1.)
    hsig500=hreg500.Clone()
    hsig500.Add(hinf500,-1.)

    # hsig150PP=hreg150.Clone()
    # hsig150PP.Add(hinf150PP,-1.)
    # hsig500PP=hreg500.Clone()
    # hsig500PP.Add(hinf500PP,-1.)

    hreg = hreg150.Clone()
    hreg.Add(hreg500,1.)

    hinf = hinf150.Clone()
    hinf.Add(hinf500,1.)

    # hinfPP = hinf150PP.Clone()
    # hinfPP.Add(hinf500PP,1.)

    hsig = hsig150.Clone()
    hsig.Add(hsig500,1.)

    # hsigPP = hsig150PP.Clone()
    # hsigPP.Add(hsig500PP,1.)

    # for h in (hreg,hinf):
    #     h.Scale( 1./h.Integral() )

    c = TCanvas("c","",1600,800)
    c.Divide(2,1)
    pad1 = c.cd(1)
    hreg.SetLineColor(kBlack)
    hinf.SetLineColor(kRed+1)
    hinf.SetLineStyle(4)
    # hinfPP.SetLineColor(kBlue+1)
    # hinfPP.SetLineStyle(2)
    for h in (hreg,hinf):
        h.SetLineWidth(2)
    # hreg.GetYaxis().SetRangeUser(0,1000)
    hreg.Draw()
    hinf.Draw("same")
    # hinfPP.Draw("same")
    # leg = pad1.BuildLegend()
    pad1.SetLogy()
    leg = TLegend(.48,.64,.68,.77)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.021)
    leg.AddEntry(hreg,"ADD Signal + SM Background","L")
    leg.AddEntry(hinf,"SM Background (LambdaT=100000)","L")
    # leg.AddEntry(hinfPP,"SM Background (PromptPhoton:ffbar2gammagamma)","L")
    leg.Draw()

    # # pad1.SetLogy()
    c.cd(2)
    hsig.SetTitle("(#Lambda_{T}=%i) - SM #gamma#gamma Background"%lt)
    # hsig.GetYaxis().SetTitle("(#Lambda_{T}=%i) - (#Lambda_{T}=#infty)"%lt)
    # print xssig
    # hsig.Scale(xssig/hsig.Integral()*LUMI)
    # hsig.GetYaxis().SetRangeUser(-0.01,0.01)
    hsig.SetLineColor(kRed+1)
    hsig.SetLineWidth(2)
    hsig.Draw()
    # hsigPP.SetLineColor(kBlue+1)
    # hsigPP.SetLineStyle(4)
    # hsigPP.SetLineWidth(2)
    # hsigPP.Draw("same")

    leg2 = TLegend(.33,.24,.53,.37)
    leg2.SetBorderSize(0)
    leg2.SetFillColor(0)
    leg2.SetFillStyle(0)
    leg2.SetTextFont(42)
    leg2.SetTextSize(0.021)
    leg2.AddEntry(hsig,"SM Background (LambdaT=100000)","L")
    # leg2.AddEntry(hsigPP,"SM Background (PromptPhoton:ffbar2gammagamma)","L")
    leg2.Draw("same")
    
    # # integral plot of background
    # pad3 = c.cd(3)
    # # print hinf.Integral()
    # hbkgint = hinf.Clone()
    # hbkgint.SetName("hbkgint")
    # hbkgint.SetTitle("")
    # endBin = hinf.GetNbinsX()+1
    # for i in range( 1, endBin):
    #     x = hinf.Integral(i,endBin)
    #     hbkgint.SetBinContent(i,x)
    # pad3.SetLogy()
    # hbkgint.Draw()

    # c.cd(4)
    # hsigint = hsig.Clone()
    # hsigint.SetName("hsigint")
    # hsigint.SetTitle("")
    # endBin = hsig.GetNbinsX()+1
    # for i in range( 1, endBin):
    #     x = hsig.Integral(i,endBin)
    #     hsigint.SetBinContent(i,x)
    # hsigint.Draw()

    c.SaveAs("dileptoncheck_massplot_LambdaT%i.png"%(lt))
    # freg.Close()
    # finf.Close()
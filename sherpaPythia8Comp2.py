print "loading ROOT..."
from ROOT import *
print "done."

gROOT.SetBatch()
gStyle.SetOptStat(0)

# build cross section dictionary
f = open('xsections_p8sherpacomparison2.txt','r')
xsDict={} # already in fb
for line in f:
    s = line.split()
    temp = "%s %s %s %s"%( s[0],s[1],s[2],s[3] )
    xsDict[temp] = float(s[4])
f.close()

faccep = open("acceptances_p8sherpacomparison2.txt",'r')
accepDict={}
for line in faccep:
    s = line.split()
    temp = "%s %s %s %s"%( s[0],s[1],s[2],s[3] )
    accepDict[temp] = float(s[4])
faccep.close()
def findXs(gen,sqrts,ms,m):

    tempString="%s %s %s %s"%( str(gen),str(sqrts),str(ms),str(m) )
    trueXS = xsDict[tempString]
    accep = accepDict[tempString]
    accep = 1. # don't weight the xs by the offline acceptance, this doesn't make sense.
    actualXS = accep*trueXS
    return actualXS

def subtractHistos(sigplusbkg,bkg):
    temp = sigplusbkg.Clone()
    temp.Add(bkg,-1.)
    return temp
def divideHistos(hist1,hist2):
    temp = hist1.Clone()
    temp.Divide(hist2)
    temp.GetYaxis().SetRangeUser(-0.5,2.)
    return temp
def plotHisto(hist,title,outfilename,leftBoundX,rightBoundX,xAxisTitle,yAxisTitle,logY):
    c = TCanvas("c","",800,800)
    hist.SetLineColor(kBlack)
    hist.SetLineWidth(2)
    hist.GetXaxis().SetRangeUser(leftBoundX,rightBoundX)
    hist.GetXaxis().SetTitle(xAxisTitle)
    hist.GetYaxis().SetTitle(yAxisTitle)
    hist.GetYaxis().SetTitleOffset(1.3)
    hist.SetTitle(title)
    hist.Draw()
    if logY:
        c.SetLogy()
    c.SaveAs(outfilename)
def plotTwoHistos(hist1,hist1label,hist2,hist2label,outfilename,leftBoundX,rightBoundX,logY,xAxisTitle,rebinFactor=1):
    c = TCanvas("c","",800,800)
    hist1.SetLineColor(kBlack)
    hist1.SetLineWidth(2)
    hist2.SetLineColor(kRed)
    hist2.SetLineStyle(4)

    hist1.Rebin(rebinFactor)
    hist2.Rebin(rebinFactor)

    hist1.GetXaxis().SetRangeUser(leftBoundX,rightBoundX)
    hist2.GetXaxis().SetRangeUser(leftBoundX,rightBoundX)

    # hist1.GetXaxis().SetTitle("M_{#gamma#gamma} (GeV)")
    hist1.GetXaxis().SetTitle(xAxisTitle)
    hist1.GetYaxis().SetTitle("Number of Events")
    hist1.GetYaxis().SetTitleOffset(1.3)

    hist1.Draw()
    hist2.Draw("same")

    leg = TLegend(.58,.64,.85,.85)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.03)
    leg.AddEntry(hist1,hist1label,"L")
    leg.AddEntry(hist2,hist2label,"L")
    leg.Draw()

    # l1 = TLatex()
    # l1.SetTextSize(0.03)
    # l1.SetTextAlign(22)
    # l1.DrawLatex(0.5,0.3,"testing 8 TeV")

    if logY:
        c.SetLogy()

    c.SaveAs(outfilename)



LUMI = 1. #fb**-1

import distroConcatenator as dc

#p8

info3000p8low_8TeV = ["ADDdiPhoton_8TeV_LambdaT3000_mHat200-750.root","analyze/hggMass",findXs("p8",8,3000,"200-750"),100000]
info3000p8mid_8TeV = ["ADDdiPhoton_8TeV_LambdaT3000_mHat750-2000.root","analyze/hggMass",findXs("p8",8,3000,"750-2000"),100000]
info3000p8high_8TeV = ["ADDdiPhoton_8TeV_LambdaT3000_mHat2000-lt.root","analyze/hggMass",findXs("p8",8,3000,"2000-lt"),100000]
info3000p8_8TeV = [info3000p8low_8TeV,info3000p8mid_8TeV,info3000p8high_8TeV]
hist3000p8_8TeV = dc.concatenate(info3000p8_8TeV,"hist3000p8_8TeV",LUMI)

info3000p8low_13TeV = ["ADDdiPhoton_13TeV_LambdaT3000_mHat200-750.root","analyze/hggMass",findXs("p8",13,3000,"200-750"),100000]
info3000p8mid_13TeV = ["ADDdiPhoton_13TeV_LambdaT3000_mHat750-2000.root","analyze/hggMass",findXs("p8",13,3000,"750-2000"),100000]
info3000p8high_13TeV = ["ADDdiPhoton_13TeV_LambdaT3000_mHat2000-lt.root","analyze/hggMass",findXs("p8",13,3000,"2000-lt"),100000]
info3000p8_13TeV = [info3000p8low_13TeV,info3000p8mid_13TeV,info3000p8high_13TeV]
hist3000p8_13TeV = dc.concatenate(info3000p8_13TeV,"hist3000p8_13TeV",LUMI)

info4000p8low_8TeV = ["ADDdiPhoton_8TeV_LambdaT4000_mHat200-750.root","analyze/hggMass",findXs("p8",8,4000,"200-750"),100000]
info4000p8mid_8TeV = ["ADDdiPhoton_8TeV_LambdaT4000_mHat750-2000.root","analyze/hggMass",findXs("p8",8,4000,"750-2000"),100000]
info4000p8high_8TeV = ["ADDdiPhoton_8TeV_LambdaT4000_mHat2000-lt.root","analyze/hggMass",findXs("p8",8,4000,"2000-lt"),100000]
info4000p8_8TeV = [info4000p8low_8TeV,info4000p8mid_8TeV,info4000p8high_8TeV]
hist4000p8_8TeV = dc.concatenate(info4000p8_8TeV,"hist4000p8_8TeV",LUMI)

info4000p8low_13TeV = ["ADDdiPhoton_13TeV_LambdaT4000_mHat200-750.root","analyze/hggMass",findXs("p8",13,4000,"200-750"),100000]
info4000p8mid_13TeV = ["ADDdiPhoton_13TeV_LambdaT4000_mHat750-2000.root","analyze/hggMass",findXs("p8",13,4000,"750-2000"),100000]
info4000p8high_13TeV = ["ADDdiPhoton_13TeV_LambdaT4000_mHat2000-lt.root","analyze/hggMass",findXs("p8",13,4000,"2000-lt"),100000]
info4000p8_13TeV = [info4000p8low_13TeV,info4000p8mid_13TeV,info4000p8high_13TeV]
hist4000p8_13TeV = dc.concatenate(info4000p8_13TeV,"hist4000p8_13TeV",LUMI)

info100000p8low_8TeV = ["ADDdiPhoton_8TeV_LambdaT100000_mHat200-750.root","analyze/hggMass",findXs("p8",8,100000,"200-750"),100000]
info100000p8mid_8TeV = ["ADDdiPhoton_8TeV_LambdaT100000_mHat750-2000.root","analyze/hggMass",findXs("p8",8,100000,"750-2000"),100000]
info100000p8high_8TeV = ["ADDdiPhoton_8TeV_LambdaT100000_mHat2000-lt.root","analyze/hggMass",findXs("p8",8,100000,"2000-lt"),100000]
info100000p8_8TeV = [info100000p8low_8TeV,info100000p8mid_8TeV,info100000p8high_8TeV]
hist100000p8_8TeV = dc.concatenate(info100000p8_8TeV,"hist100000p8_8TeV",LUMI)

info100000p8low_13TeV = ["ADDdiPhoton_13TeV_LambdaT100000_mHat200-750.root","analyze/hggMass",findXs("p8",13,100000,"200-750"),100000]
info100000p8mid_13TeV = ["ADDdiPhoton_13TeV_LambdaT100000_mHat750-2000.root","analyze/hggMass",findXs("p8",13,100000,"750-2000"),100000]
info100000p8high_13TeV = ["ADDdiPhoton_13TeV_LambdaT100000_mHat2000-lt.root","analyze/hggMass",findXs("p8",13,100000,"2000-lt"),100000]
info100000p8_13TeV = [info100000p8low_13TeV,info100000p8mid_13TeV,info100000p8high_13TeV]
hist100000p8_13TeV = dc.concatenate(info100000p8_13TeV,"hist100000p8_13TeV",LUMI)


# Sherpa

info3000sherpalow_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hggMass",findXs("sherpa",8,3000,"200-750"),100000]
info3000sherpamid_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hggMass",findXs("sherpa",8,3000,"750-2000"),100000]
info3000sherpahigh_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hggMass",findXs("sherpa",8,3000,"2000-ms"),100000]
info3000sherpa_8TeV = [info3000sherpalow_8TeV,info3000sherpamid_8TeV,info3000sherpahigh_8TeV]
hist3000sherpa_8TeV = dc.concatenate(info3000sherpa_8TeV,"hist3000sherpa_8TeV",LUMI)

info3000sherpalow_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hggMass",findXs("sherpa",13,3000,"200-750"),100000]
info3000sherpamid_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hggMass",findXs("sherpa",13,3000,"750-2000"),100000]
info3000sherpahigh_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hggMass",findXs("sherpa",13,3000,"2000-ms"),100000]
info3000sherpa_13TeV = [info3000sherpalow_13TeV,info3000sherpamid_13TeV,info3000sherpahigh_13TeV]
hist3000sherpa_13TeV = dc.concatenate(info3000sherpa_13TeV,"hist3000sherpa_13TeV",LUMI)

info4000sherpalow_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hggMass",findXs("sherpa",8,4000,"200-750"),100000]
info4000sherpamid_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hggMass",findXs("sherpa",8,4000,"750-2000"),100000]
info4000sherpahigh_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hggMass",findXs("sherpa",8,4000,"2000-ms"),100000]
info4000sherpa_8TeV = [info4000sherpalow_8TeV,info4000sherpamid_8TeV,info4000sherpahigh_8TeV]
hist4000sherpa_8TeV = dc.concatenate(info4000sherpa_8TeV,"hist4000sherpa_8TeV",LUMI)

info4000sherpalow_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hggMass",findXs("sherpa",13,4000,"200-750"),100000]
info4000sherpamid_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hggMass",findXs("sherpa",13,4000,"750-2000"),100000]
info4000sherpahigh_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hggMass",findXs("sherpa",13,4000,"2000-ms"),100000]
info4000sherpa_13TeV = [info4000sherpalow_13TeV,info4000sherpamid_13TeV,info4000sherpahigh_13TeV]
hist4000sherpa_13TeV = dc.concatenate(info4000sherpa_13TeV,"hist4000sherpa_13TeV",LUMI)

info100000sherpalow_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hggMass",findXs("sherpa",8,100000,"200-750"),100000]
info100000sherpamid_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hggMass",findXs("sherpa",8,100000,"750-2000"),100000]
info100000sherpahigh_8TeV = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hggMass",findXs("sherpa",8,100000,"2000-ms"),100000]
info100000sherpa_8TeV = [info100000sherpalow_8TeV,info100000sherpamid_8TeV,info100000sherpahigh_8TeV]
hist100000sherpa_8TeV = dc.concatenate(info100000sherpa_8TeV,"hist100000sherpa_8TeV",LUMI)

info100000sherpalow_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hggMass",findXs("sherpa",13,100000,"200-750"),100000]
info100000sherpamid_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hggMass",findXs("sherpa",13,100000,"750-2000"),100000]
info100000sherpahigh_13TeV = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hggMass",findXs("sherpa",13,100000,"2000-ms"),100000]
info100000sherpa_13TeV = [info100000sherpalow_13TeV,info100000sherpamid_13TeV,info100000sherpahigh_13TeV]
hist100000sherpa_13TeV = dc.concatenate(info100000sherpa_13TeV,"hist100000sherpa_13TeV",LUMI)

sighist3000p8_8TeV = subtractHistos(hist3000p8_8TeV,hist100000p8_8TeV)
sighist3000p8_13TeV = subtractHistos(hist3000p8_13TeV,hist100000p8_13TeV)

sighist4000p8_8TeV = subtractHistos(hist4000p8_8TeV,hist100000p8_8TeV)
sighist4000p8_13TeV = subtractHistos(hist4000p8_13TeV,hist100000p8_13TeV)

sighist3000sherpa_8TeV = subtractHistos(hist3000sherpa_8TeV,hist100000sherpa_8TeV)
sighist3000sherpa_13TeV = subtractHistos(hist3000sherpa_13TeV,hist100000sherpa_13TeV)

sighist4000sherpa_8TeV = subtractHistos(hist4000sherpa_8TeV,hist100000sherpa_8TeV)
sighist4000sherpa_13TeV = subtractHistos(hist4000sherpa_13TeV,hist100000sherpa_13TeV)

sigcomp3000_8TeV = divideHistos(sighist3000sherpa_8TeV,sighist3000p8_8TeV)
sigcomp4000_8TeV = divideHistos(sighist4000sherpa_8TeV,sighist4000p8_8TeV)
sigcomp3000_13TeV = divideHistos(sighist3000sherpa_13TeV,sighist3000p8_13TeV)
sigcomp4000_13TeV = divideHistos(sighist4000sherpa_13TeV,sighist4000p8_13TeV)

plotHisto(sigcomp3000_8TeV,"","p8sherpacomp_8TeV_sigratio_ms3000.pdf",0.,3100.,"M_{#gamma#gamma} (GeV)","Sherpa/Pythia8",False)
plotHisto(sigcomp3000_13TeV,"","p8sherpacomp_13TeV_sigratio_ms3000.pdf",0.,3100.,"M_{#gamma#gamma} (GeV)","Sherpa/Pythia8",False)
plotHisto(sigcomp4000_8TeV,"","p8sherpacomp_8TeV_sigratio_ms4000.pdf",0.,4100.,"M_{#gamma#gamma} (GeV)","Sherpa/Pythia8",False)
plotHisto(sigcomp4000_13TeV,"","p8sherpacomp_13TeV_sigratio_ms4000.pdf",0.,4100.,"M_{#gamma#gamma} (GeV)","Sherpa/Pythia8",False)

# SetRangeUser for signal histograms
# for h in (sighist3000p8_8TeV,sighist3000sherpa_8TeV):
#     # h.GetXaxis().SetRangeUser(750., h.GetBinLowEdge( h.GetNbinsX()+1 ) )
#     h.GetYaxis().SetRangeUser(0.,0.25)
# for h in (sighist4000p8_8TeV,sighist4000sherpa_8TeV):
#     h.GetYaxis().SetRangeUser(0.,0.08)
# for h in (sighist3000p8_13TeV,sighist3000sherpa_13TeV):
#     # h.GetXaxis().SetRangeUser(750., h.GetBinLowEdge( h.GetNbinsX()+1 ) )
#     h.GetYaxis().SetRangeUser(0.,2.)
# for h in (sighist4000p8_13TeV,sighist4000sherpa_13TeV):
#     # h.GetXaxis().SetRangeUser(750., h.GetBinLowEdge( h.GetNbinsX()+1 ) )
#     h.GetYaxis().SetRangeUser(0.,0.18)

# pT and eta distributions

# newtfile = TFile("plotsForAndrew.root","recreate")
# newtfile.cd()
# for h in [hist3000p8_8TeV,hist3000p8_13TeV,hist3000sherpa_8TeV,hist3000sherpa_13TeV,hist4000p8_8TeV,hist4000p8_13TeV,hist4000sherpa_8TeV,hist4000sherpa_13TeV,hist100000p8_8TeV,hist100000p8_13TeV,hist100000sherpa_8TeV,hist100000sherpa_13TeV]:
#     h.Write()
# newtfile.Close()

plotTwoHistos(hist3000p8_8TeV,"Pythia 8 (8 TeV)",hist3000sherpa_8TeV,"Sherpa (8 TeV)","p8sherpacomp_8TeV_ms3000.pdf",0.,3100.,True,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(sighist3000p8_8TeV,"Pythia 8 (8 TeV)",sighist3000sherpa_8TeV,"Sherpa (8 TeV)","p8sherpacomp_8TeV_sig_ms3000.pdf",0.,3100.,False,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(hist3000p8_13TeV,"Pythia 8 (13 TeV)",hist3000sherpa_13TeV,"Sherpa (13 TeV)","p8sherpacomp_13TeV_ms3000.pdf",0.,3100.,True,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(sighist3000p8_13TeV,"Pythia 8 (13 TeV)",sighist3000sherpa_13TeV,"Sherpa (13 TeV)","p8sherpacomp_13TeV_sig_ms3000.pdf",0.,3100.,False,"M_{#gamma#gamma} (GeV)")

plotTwoHistos(hist4000p8_8TeV,"Pythia 8 (8 TeV)",hist4000sherpa_8TeV,"Sherpa (8 TeV)","p8sherpacomp_8TeV_ms4000.pdf",0.,4100.,True,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(sighist4000p8_8TeV,"Pythia 8 (8 TeV)",sighist4000sherpa_8TeV,"Sherpa (8 TeV)","p8sherpacomp_8TeV_sig_ms4000.pdf",0.,4100.,False,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(hist4000p8_13TeV,"Pythia 8 (13 TeV)",hist4000sherpa_13TeV,"Sherpa (13 TeV)","p8sherpacomp_13TeV_ms4000.pdf",0.,4100.,True,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(sighist4000p8_13TeV,"Pythia 8 (13 TeV)",sighist4000sherpa_13TeV,"Sherpa (13 TeV)","p8sherpacomp_13TeV_sig_ms4000.pdf",0.,4100.,False,"M_{#gamma#gamma} (GeV)")

plotTwoHistos(hist100000p8_8TeV,"Pythia 8 (8 TeV)",hist100000sherpa_8TeV,"Sherpa (8 TeV)","p8sherpacomp_8TeV_ms100000.pdf",0.,4200.,True,"M_{#gamma#gamma} (GeV)")
plotTwoHistos(hist100000p8_13TeV,"Pythia 8 (13 TeV)",hist100000sherpa_13TeV,"Sherpa (13 TeV)","p8sherpacomp_13TeV_ms100000.pdf",0.,5600.,True,"M_{#gamma#gamma} (GeV)")


# leading pT

info3000p8low_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat200-750.root","analyze/hleadingPhoPt",findXs("p8",8,3000,"200-750"),100000]
info3000p8mid_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat750-2000.root","analyze/hleadingPhoPt",findXs("p8",8,3000,"750-2000"),100000]
info3000p8high_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat2000-lt.root","analyze/hleadingPhoPt",findXs("p8",8,3000,"2000-lt"),100000]
info3000p8_8TeV_pT0_aftercuts = [info3000p8low_8TeV_pT0_aftercuts,info3000p8mid_8TeV_pT0_aftercuts,info3000p8high_8TeV_pT0_aftercuts]
hist3000p8_8TeV_pT0_aftercuts = dc.concatenate(info3000p8_8TeV_pT0_aftercuts,"hist3000p8_8TeV_pT0_aftercuts",LUMI)

info3000p8low_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat200-750.root","analyze/hleadingPhoPt",findXs("p8",13,3000,"200-750"),100000]
info3000p8mid_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat750-2000.root","analyze/hleadingPhoPt",findXs("p8",13,3000,"750-2000"),100000]
info3000p8high_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat2000-lt.root","analyze/hleadingPhoPt",findXs("p8",13,3000,"2000-lt"),100000]
info3000p8_13TeV_pT0_aftercuts = [info3000p8low_13TeV_pT0_aftercuts,info3000p8mid_13TeV_pT0_aftercuts,info3000p8high_13TeV_pT0_aftercuts]
hist3000p8_13TeV_pT0_aftercuts = dc.concatenate(info3000p8_13TeV_pT0_aftercuts,"hist3000p8_13TeV_pT0_aftercuts",LUMI)

info4000p8low_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat200-750.root","analyze/hleadingPhoPt",findXs("p8",8,4000,"200-750"),100000]
info4000p8mid_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat750-2000.root","analyze/hleadingPhoPt",findXs("p8",8,4000,"750-2000"),100000]
info4000p8high_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat2000-lt.root","analyze/hleadingPhoPt",findXs("p8",8,4000,"2000-lt"),100000]
info4000p8_8TeV_pT0_aftercuts = [info4000p8low_8TeV_pT0_aftercuts,info4000p8mid_8TeV_pT0_aftercuts,info4000p8high_8TeV_pT0_aftercuts]
hist4000p8_8TeV_pT0_aftercuts = dc.concatenate(info4000p8_8TeV_pT0_aftercuts,"hist4000p8_8TeV_pT0_aftercuts",LUMI)

info4000p8low_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat200-750.root","analyze/hleadingPhoPt",findXs("p8",13,4000,"200-750"),100000]
info4000p8mid_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat750-2000.root","analyze/hleadingPhoPt",findXs("p8",13,4000,"750-2000"),100000]
info4000p8high_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat2000-lt.root","analyze/hleadingPhoPt",findXs("p8",13,4000,"2000-lt"),100000]
info4000p8_13TeV_pT0_aftercuts = [info4000p8low_13TeV_pT0_aftercuts,info4000p8mid_13TeV_pT0_aftercuts,info4000p8high_13TeV_pT0_aftercuts]
hist4000p8_13TeV_pT0_aftercuts = dc.concatenate(info4000p8_13TeV_pT0_aftercuts,"hist4000p8_13TeV_pT0_aftercuts",LUMI)

info100000p8low_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat200-750.root","analyze/hleadingPhoPt",findXs("p8",8,100000,"200-750"),100000]
info100000p8mid_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat750-2000.root","analyze/hleadingPhoPt",findXs("p8",8,100000,"750-2000"),100000]
info100000p8high_8TeV_pT0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat2000-lt.root","analyze/hleadingPhoPt",findXs("p8",8,100000,"2000-lt"),100000]
info100000p8_8TeV_pT0_aftercuts = [info100000p8low_8TeV_pT0_aftercuts,info100000p8mid_8TeV_pT0_aftercuts,info100000p8high_8TeV_pT0_aftercuts]
hist100000p8_8TeV_pT0_aftercuts = dc.concatenate(info100000p8_8TeV_pT0_aftercuts,"hist100000p8_8TeV_pT0_aftercuts",LUMI)

info100000p8low_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat200-750.root","analyze/hleadingPhoPt",findXs("p8",13,100000,"200-750"),100000]
info100000p8mid_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat750-2000.root","analyze/hleadingPhoPt",findXs("p8",13,100000,"750-2000"),100000]
info100000p8high_13TeV_pT0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat2000-lt.root","analyze/hleadingPhoPt",findXs("p8",13,100000,"2000-lt"),100000]
info100000p8_13TeV_pT0_aftercuts = [info100000p8low_13TeV_pT0_aftercuts,info100000p8mid_13TeV_pT0_aftercuts,info100000p8high_13TeV_pT0_aftercuts]
hist100000p8_13TeV_pT0_aftercuts = dc.concatenate(info100000p8_13TeV_pT0_aftercuts,"hist100000p8_13TeV_pT0_aftercuts",LUMI)

# Sherpa

info3000sherpalow_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hleadingPhoPt",findXs("sherpa",8,3000,"200-750"),100000]
info3000sherpamid_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hleadingPhoPt",findXs("sherpa",8,3000,"750-2000"),100000]
info3000sherpahigh_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hleadingPhoPt",findXs("sherpa",8,3000,"2000-ms"),100000]
info3000sherpa_8TeV_pT0_aftercuts = [info3000sherpalow_8TeV_pT0_aftercuts,info3000sherpamid_8TeV_pT0_aftercuts,info3000sherpahigh_8TeV_pT0_aftercuts]
hist3000sherpa_8TeV_pT0_aftercuts = dc.concatenate(info3000sherpa_8TeV_pT0_aftercuts,"hist3000sherpa_8TeV_pT0_aftercuts",LUMI)

info3000sherpalow_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hleadingPhoPt",findXs("sherpa",13,3000,"200-750"),100000]
info3000sherpamid_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hleadingPhoPt",findXs("sherpa",13,3000,"750-2000"),100000]
info3000sherpahigh_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hleadingPhoPt",findXs("sherpa",13,3000,"2000-ms"),100000]
info3000sherpa_13TeV_pT0_aftercuts = [info3000sherpalow_13TeV_pT0_aftercuts,info3000sherpamid_13TeV_pT0_aftercuts,info3000sherpahigh_13TeV_pT0_aftercuts]
hist3000sherpa_13TeV_pT0_aftercuts = dc.concatenate(info3000sherpa_13TeV_pT0_aftercuts,"hist3000sherpa_13TeV_pT0_aftercuts",LUMI)

info4000sherpalow_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hleadingPhoPt",findXs("sherpa",8,4000,"200-750"),100000]
info4000sherpamid_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hleadingPhoPt",findXs("sherpa",8,4000,"750-2000"),100000]
info4000sherpahigh_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hleadingPhoPt",findXs("sherpa",8,4000,"2000-ms"),100000]
info4000sherpa_8TeV_pT0_aftercuts = [info4000sherpalow_8TeV_pT0_aftercuts,info4000sherpamid_8TeV_pT0_aftercuts,info4000sherpahigh_8TeV_pT0_aftercuts]
hist4000sherpa_8TeV_pT0_aftercuts = dc.concatenate(info4000sherpa_8TeV_pT0_aftercuts,"hist4000sherpa_8TeV_pT0_aftercuts",LUMI)

info4000sherpalow_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hleadingPhoPt",findXs("sherpa",13,4000,"200-750"),100000]
info4000sherpamid_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hleadingPhoPt",findXs("sherpa",13,4000,"750-2000"),100000]
info4000sherpahigh_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hleadingPhoPt",findXs("sherpa",13,4000,"2000-ms"),100000]
info4000sherpa_13TeV_pT0_aftercuts = [info4000sherpalow_13TeV_pT0_aftercuts,info4000sherpamid_13TeV_pT0_aftercuts,info4000sherpahigh_13TeV_pT0_aftercuts]
hist4000sherpa_13TeV_pT0_aftercuts = dc.concatenate(info4000sherpa_13TeV_pT0_aftercuts,"hist4000sherpa_13TeV_pT0_aftercuts",LUMI)

info100000sherpalow_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hleadingPhoPt",findXs("sherpa",8,100000,"200-750"),100000]
info100000sherpamid_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hleadingPhoPt",findXs("sherpa",8,100000,"750-2000"),100000]
info100000sherpahigh_8TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hleadingPhoPt",findXs("sherpa",8,100000,"2000-ms"),100000]
info100000sherpa_8TeV_pT0_aftercuts = [info100000sherpalow_8TeV_pT0_aftercuts,info100000sherpamid_8TeV_pT0_aftercuts,info100000sherpahigh_8TeV_pT0_aftercuts]
hist100000sherpa_8TeV_pT0_aftercuts = dc.concatenate(info100000sherpa_8TeV_pT0_aftercuts,"hist100000sherpa_8TeV_pT0_aftercuts",LUMI)

info100000sherpalow_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hleadingPhoPt",findXs("sherpa",13,100000,"200-750"),100000]
info100000sherpamid_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hleadingPhoPt",findXs("sherpa",13,100000,"750-2000"),100000]
info100000sherpahigh_13TeV_pT0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hleadingPhoPt",findXs("sherpa",13,100000,"2000-ms"),100000]
info100000sherpa_13TeV_pT0_aftercuts = [info100000sherpalow_13TeV_pT0_aftercuts,info100000sherpamid_13TeV_pT0_aftercuts,info100000sherpahigh_13TeV_pT0_aftercuts]
hist1000sherpa_13TeV_pT0_aftercuts = dc.concatenate(info100000sherpa_13TeV_pT0_aftercuts,"hist100000sherpa_13TeV_pT0_aftercuts",LUMI)

plotTwoHistos(hist3000p8_8TeV_pT0_aftercuts,"Pythia 8 (8 TeV)",hist3000sherpa_8TeV_pT0_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_pT0_aftercuts_ms3000.pdf",0.,3100.,True,"Leading Photon pT (GeV)",4)
plotTwoHistos(hist3000p8_13TeV_pT0_aftercuts,"Pythia 8 (13 TeV)",hist3000sherpa_13TeV_pT0_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_pT0_aftercuts_ms3000.pdf",0.,3100.,True,"Leading Photon pT (GeV)",4)

plotTwoHistos(hist4000p8_8TeV_pT0_aftercuts,"Pythia 8 (8 TeV)",hist4000sherpa_8TeV_pT0_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_pT0_aftercuts_ms4000.pdf",0.,4100.,True,"Leading Photon pT (GeV)",4)
plotTwoHistos(hist4000p8_13TeV_pT0_aftercuts,"Pythia 8 (13 TeV)",hist4000sherpa_13TeV_pT0_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_pT0_aftercuts_ms4000.pdf",0.,4100.,True,"Leading Photon pT (GeV)",4)

plotTwoHistos(hist100000p8_8TeV_pT0_aftercuts,"Pythia 8 (8 TeV)",hist100000sherpa_8TeV_pT0_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_pT0_aftercuts_ms100000.pdf",0.,4200.,True,"Leading Photon pT (GeV)",4)
plotTwoHistos(hist100000p8_13TeV_pT0_aftercuts,"Pythia 8 (13 TeV)",hist100000sherpa_13TeV_pT0_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_pT0_aftercuts_ms100000.pdf",0.,5600.,True,"Leading Photon pT (GeV)",4)

# subleading pT

info3000p8low_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat200-750.root","analyze/hsubleadingPhoPt",findXs("p8",8,3000,"200-750"),100000]
info3000p8mid_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat750-2000.root","analyze/hsubleadingPhoPt",findXs("p8",8,3000,"750-2000"),100000]
info3000p8high_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat2000-lt.root","analyze/hsubleadingPhoPt",findXs("p8",8,3000,"2000-lt"),100000]
info3000p8_8TeV_pT1_aftercuts = [info3000p8low_8TeV_pT1_aftercuts,info3000p8mid_8TeV_pT1_aftercuts,info3000p8high_8TeV_pT1_aftercuts]
hist3000p8_8TeV_pT1_aftercuts = dc.concatenate(info3000p8_8TeV_pT1_aftercuts,"hist3000p8_8TeV_pT1_aftercuts",LUMI)

info3000p8low_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat200-750.root","analyze/hsubleadingPhoPt",findXs("p8",13,3000,"200-750"),100000]
info3000p8mid_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat750-2000.root","analyze/hsubleadingPhoPt",findXs("p8",13,3000,"750-2000"),100000]
info3000p8high_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat2000-lt.root","analyze/hsubleadingPhoPt",findXs("p8",13,3000,"2000-lt"),100000]
info3000p8_13TeV_pT1_aftercuts = [info3000p8low_13TeV_pT1_aftercuts,info3000p8mid_13TeV_pT1_aftercuts,info3000p8high_13TeV_pT1_aftercuts]
hist3000p8_13TeV_pT1_aftercuts = dc.concatenate(info3000p8_13TeV_pT1_aftercuts,"hist3000p8_13TeV_pT1_aftercuts",LUMI)

info4000p8low_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat200-750.root","analyze/hsubleadingPhoPt",findXs("p8",8,4000,"200-750"),100000]
info4000p8mid_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat750-2000.root","analyze/hsubleadingPhoPt",findXs("p8",8,4000,"750-2000"),100000]
info4000p8high_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat2000-lt.root","analyze/hsubleadingPhoPt",findXs("p8",8,4000,"2000-lt"),100000]
info4000p8_8TeV_pT1_aftercuts = [info4000p8low_8TeV_pT1_aftercuts,info4000p8mid_8TeV_pT1_aftercuts,info4000p8high_8TeV_pT1_aftercuts]
hist4000p8_8TeV_pT1_aftercuts = dc.concatenate(info4000p8_8TeV_pT1_aftercuts,"hist4000p8_8TeV_pT1_aftercuts",LUMI)

info4000p8low_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat200-750.root","analyze/hsubleadingPhoPt",findXs("p8",13,4000,"200-750"),100000]
info4000p8mid_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat750-2000.root","analyze/hsubleadingPhoPt",findXs("p8",13,4000,"750-2000"),100000]
info4000p8high_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat2000-lt.root","analyze/hsubleadingPhoPt",findXs("p8",13,4000,"2000-lt"),100000]
info4000p8_13TeV_pT1_aftercuts = [info4000p8low_13TeV_pT1_aftercuts,info4000p8mid_13TeV_pT1_aftercuts,info4000p8high_13TeV_pT1_aftercuts]
hist4000p8_13TeV_pT1_aftercuts = dc.concatenate(info4000p8_13TeV_pT1_aftercuts,"hist4000p8_13TeV_pT1_aftercuts",LUMI)

info100000p8low_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat200-750.root","analyze/hsubleadingPhoPt",findXs("p8",8,100000,"200-750"),100000]
info100000p8mid_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat750-2000.root","analyze/hsubleadingPhoPt",findXs("p8",8,100000,"750-2000"),100000]
info100000p8high_8TeV_pT1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat2000-lt.root","analyze/hsubleadingPhoPt",findXs("p8",8,100000,"2000-lt"),100000]
info100000p8_8TeV_pT1_aftercuts = [info100000p8low_8TeV_pT1_aftercuts,info100000p8mid_8TeV_pT1_aftercuts,info100000p8high_8TeV_pT1_aftercuts]
hist100000p8_8TeV_pT1_aftercuts = dc.concatenate(info100000p8_8TeV_pT1_aftercuts,"hist100000p8_8TeV_pT1_aftercuts",LUMI)

info100000p8low_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat200-750.root","analyze/hsubleadingPhoPt",findXs("p8",13,100000,"200-750"),100000]
info100000p8mid_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat750-2000.root","analyze/hsubleadingPhoPt",findXs("p8",13,100000,"750-2000"),100000]
info100000p8high_13TeV_pT1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat2000-lt.root","analyze/hsubleadingPhoPt",findXs("p8",13,100000,"2000-lt"),100000]
info100000p8_13TeV_pT1_aftercuts = [info100000p8low_13TeV_pT1_aftercuts,info100000p8mid_13TeV_pT1_aftercuts,info100000p8high_13TeV_pT1_aftercuts]
hist100000p8_13TeV_pT1_aftercuts = dc.concatenate(info100000p8_13TeV_pT1_aftercuts,"hist100000p8_13TeV_pT1_aftercuts",LUMI)

# Sherpa

info3000sherpalow_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,3000,"200-750"),100000]
info3000sherpamid_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,3000,"750-2000"),100000]
info3000sherpahigh_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,3000,"2000-ms"),100000]
info3000sherpa_8TeV_pT1_aftercuts = [info3000sherpalow_8TeV_pT1_aftercuts,info3000sherpamid_8TeV_pT1_aftercuts,info3000sherpahigh_8TeV_pT1_aftercuts]
hist3000sherpa_8TeV_pT1_aftercuts = dc.concatenate(info3000sherpa_8TeV_pT1_aftercuts,"hist3000sherpa_8TeV_pT1_aftercuts",LUMI)

info3000sherpalow_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,3000,"200-750"),100000]
info3000sherpamid_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,3000,"750-2000"),100000]
info3000sherpahigh_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,3000,"2000-ms"),100000]
info3000sherpa_13TeV_pT1_aftercuts = [info3000sherpalow_13TeV_pT1_aftercuts,info3000sherpamid_13TeV_pT1_aftercuts,info3000sherpahigh_13TeV_pT1_aftercuts]
hist3000sherpa_13TeV_pT1_aftercuts = dc.concatenate(info3000sherpa_13TeV_pT1_aftercuts,"hist3000sherpa_13TeV_pT1_aftercuts",LUMI)

info4000sherpalow_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,4000,"200-750"),100000]
info4000sherpamid_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,4000,"750-2000"),100000]
info4000sherpahigh_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,4000,"2000-ms"),100000]
info4000sherpa_8TeV_pT1_aftercuts = [info4000sherpalow_8TeV_pT1_aftercuts,info4000sherpamid_8TeV_pT1_aftercuts,info4000sherpahigh_8TeV_pT1_aftercuts]
hist4000sherpa_8TeV_pT1_aftercuts = dc.concatenate(info4000sherpa_8TeV_pT1_aftercuts,"hist4000sherpa_8TeV_pT1_aftercuts",LUMI)

info4000sherpalow_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,4000,"200-750"),100000]
info4000sherpamid_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,4000,"750-2000"),100000]
info4000sherpahigh_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,4000,"2000-ms"),100000]
info4000sherpa_13TeV_pT1_aftercuts = [info4000sherpalow_13TeV_pT1_aftercuts,info4000sherpamid_13TeV_pT1_aftercuts,info4000sherpahigh_13TeV_pT1_aftercuts]
hist4000sherpa_13TeV_pT1_aftercuts = dc.concatenate(info4000sherpa_13TeV_pT1_aftercuts,"hist4000sherpa_13TeV_pT1_aftercuts",LUMI)

info100000sherpalow_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,100000,"200-750"),100000]
info100000sherpamid_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,100000,"750-2000"),100000]
info100000sherpahigh_8TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hsubleadingPhoPt",findXs("sherpa",8,100000,"2000-ms"),100000]
info100000sherpa_8TeV_pT1_aftercuts = [info100000sherpalow_8TeV_pT1_aftercuts,info100000sherpamid_8TeV_pT1_aftercuts,info100000sherpahigh_8TeV_pT1_aftercuts]
hist100000sherpa_8TeV_pT1_aftercuts = dc.concatenate(info100000sherpa_8TeV_pT1_aftercuts,"hist100000sherpa_8TeV_pT1_aftercuts",LUMI)

info100000sherpalow_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,100000,"200-750"),100000]
info100000sherpamid_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,100000,"750-2000"),100000]
info100000sherpahigh_13TeV_pT1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hsubleadingPhoPt",findXs("sherpa",13,100000,"2000-ms"),100000]
info100000sherpa_13TeV_pT1_aftercuts = [info100000sherpalow_13TeV_pT1_aftercuts,info100000sherpamid_13TeV_pT1_aftercuts,info100000sherpahigh_13TeV_pT1_aftercuts]
hist1000sherpa_13TeV_pT1_aftercuts = dc.concatenate(info100000sherpa_13TeV_pT1_aftercuts,"hist100000sherpa_13TeV_pT1_aftercuts",LUMI)

plotTwoHistos(hist3000p8_8TeV_pT1_aftercuts,"Pythia 8 (8 TeV)",hist3000sherpa_8TeV_pT1_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_pT1_aftercuts_ms3000.pdf",0.,3100.,True,"Subleading Photon pT (GeV)",4)
plotTwoHistos(hist3000p8_13TeV_pT1_aftercuts,"Pythia 8 (13 TeV)",hist3000sherpa_13TeV_pT1_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_pT1_aftercuts_ms3000.pdf",0.,3100.,True,"Subleading Photon pT (GeV)",4)

plotTwoHistos(hist4000p8_8TeV_pT1_aftercuts,"Pythia 8 (8 TeV)",hist4000sherpa_8TeV_pT1_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_pT1_aftercuts_ms4000.pdf",0.,4100.,True,"Subleading Photon pT (GeV)",4)
plotTwoHistos(hist4000p8_13TeV_pT1_aftercuts,"Pythia 8 (13 TeV)",hist4000sherpa_13TeV_pT1_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_pT1_aftercuts_ms4000.pdf",0.,4100.,True,"Subleading Photon pT (GeV)",4)

plotTwoHistos(hist100000p8_8TeV_pT1_aftercuts,"Pythia 8 (8 TeV)",hist100000sherpa_8TeV_pT1_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_pT1_aftercuts_ms100000.pdf",0.,4200.,True,"Subleading Photon pT (GeV)",4)
plotTwoHistos(hist100000p8_13TeV_pT1_aftercuts,"Pythia 8 (13 TeV)",hist100000sherpa_13TeV_pT1_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_pT1_aftercuts_ms100000.pdf",0.,5600.,True,"Subleading Photon pT (GeV)",4)

#leading eta

info3000p8low_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat200-750.root","analyze/hleadingPhoEta",findXs("p8",8,3000,"200-750"),100000]
info3000p8mid_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat750-2000.root","analyze/hleadingPhoEta",findXs("p8",8,3000,"750-2000"),100000]
info3000p8high_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat2000-lt.root","analyze/hleadingPhoEta",findXs("p8",8,3000,"2000-lt"),100000]
info3000p8_8TeV_eta0_aftercuts = [info3000p8low_8TeV_eta0_aftercuts,info3000p8mid_8TeV_eta0_aftercuts,info3000p8high_8TeV_eta0_aftercuts]
hist3000p8_8TeV_eta0_aftercuts = dc.concatenate(info3000p8_8TeV_eta0_aftercuts,"hist3000p8_8TeV_eta0_aftercuts",LUMI)

info3000p8low_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat200-750.root","analyze/hleadingPhoEta",findXs("p8",13,3000,"200-750"),100000]
info3000p8mid_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat750-2000.root","analyze/hleadingPhoEta",findXs("p8",13,3000,"750-2000"),100000]
info3000p8high_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat2000-lt.root","analyze/hleadingPhoEta",findXs("p8",13,3000,"2000-lt"),100000]
info3000p8_13TeV_eta0_aftercuts = [info3000p8low_13TeV_eta0_aftercuts,info3000p8mid_13TeV_eta0_aftercuts,info3000p8high_13TeV_eta0_aftercuts]
hist3000p8_13TeV_eta0_aftercuts = dc.concatenate(info3000p8_13TeV_eta0_aftercuts,"hist3000p8_13TeV_eta0_aftercuts",LUMI)

info4000p8low_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat200-750.root","analyze/hleadingPhoEta",findXs("p8",8,4000,"200-750"),100000]
info4000p8mid_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat750-2000.root","analyze/hleadingPhoEta",findXs("p8",8,4000,"750-2000"),100000]
info4000p8high_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat2000-lt.root","analyze/hleadingPhoEta",findXs("p8",8,4000,"2000-lt"),100000]
info4000p8_8TeV_eta0_aftercuts = [info4000p8low_8TeV_eta0_aftercuts,info4000p8mid_8TeV_eta0_aftercuts,info4000p8high_8TeV_eta0_aftercuts]
hist4000p8_8TeV_eta0_aftercuts = dc.concatenate(info4000p8_8TeV_eta0_aftercuts,"hist4000p8_8TeV_eta0_aftercuts",LUMI)

info4000p8low_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat200-750.root","analyze/hleadingPhoEta",findXs("p8",13,4000,"200-750"),100000]
info4000p8mid_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat750-2000.root","analyze/hleadingPhoEta",findXs("p8",13,4000,"750-2000"),100000]
info4000p8high_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat2000-lt.root","analyze/hleadingPhoEta",findXs("p8",13,4000,"2000-lt"),100000]
info4000p8_13TeV_eta0_aftercuts = [info4000p8low_13TeV_eta0_aftercuts,info4000p8mid_13TeV_eta0_aftercuts,info4000p8high_13TeV_eta0_aftercuts]
hist4000p8_13TeV_eta0_aftercuts = dc.concatenate(info4000p8_13TeV_eta0_aftercuts,"hist4000p8_13TeV_eta0_aftercuts",LUMI)

info100000p8low_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat200-750.root","analyze/hleadingPhoEta",findXs("p8",8,100000,"200-750"),100000]
info100000p8mid_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat750-2000.root","analyze/hleadingPhoEta",findXs("p8",8,100000,"750-2000"),100000]
info100000p8high_8TeV_eta0_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat2000-lt.root","analyze/hleadingPhoEta",findXs("p8",8,100000,"2000-lt"),100000]
info100000p8_8TeV_eta0_aftercuts = [info100000p8low_8TeV_eta0_aftercuts,info100000p8mid_8TeV_eta0_aftercuts,info100000p8high_8TeV_eta0_aftercuts]
hist100000p8_8TeV_eta0_aftercuts = dc.concatenate(info100000p8_8TeV_eta0_aftercuts,"hist100000p8_8TeV_eta0_aftercuts",LUMI)

info100000p8low_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat200-750.root","analyze/hleadingPhoEta",findXs("p8",13,100000,"200-750"),100000]
info100000p8mid_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat750-2000.root","analyze/hleadingPhoEta",findXs("p8",13,100000,"750-2000"),100000]
info100000p8high_13TeV_eta0_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat2000-lt.root","analyze/hleadingPhoEta",findXs("p8",13,100000,"2000-lt"),100000]
info100000p8_13TeV_eta0_aftercuts = [info100000p8low_13TeV_eta0_aftercuts,info100000p8mid_13TeV_eta0_aftercuts,info100000p8high_13TeV_eta0_aftercuts]
hist100000p8_13TeV_eta0_aftercuts = dc.concatenate(info100000p8_13TeV_eta0_aftercuts,"hist100000p8_13TeV_eta0_aftercuts",LUMI)

# Sherpa

info3000sherpalow_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hleadingPhoEta",findXs("sherpa",8,3000,"200-750"),100000]
info3000sherpamid_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hleadingPhoEta",findXs("sherpa",8,3000,"750-2000"),100000]
info3000sherpahigh_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hleadingPhoEta",findXs("sherpa",8,3000,"2000-ms"),100000]
info3000sherpa_8TeV_eta0_aftercuts = [info3000sherpalow_8TeV_eta0_aftercuts,info3000sherpamid_8TeV_eta0_aftercuts,info3000sherpahigh_8TeV_eta0_aftercuts]
hist3000sherpa_8TeV_eta0_aftercuts = dc.concatenate(info3000sherpa_8TeV_eta0_aftercuts,"hist3000sherpa_8TeV_eta0_aftercuts",LUMI)

info3000sherpalow_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hleadingPhoEta",findXs("sherpa",13,3000,"200-750"),100000]
info3000sherpamid_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hleadingPhoEta",findXs("sherpa",13,3000,"750-2000"),100000]
info3000sherpahigh_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hleadingPhoEta",findXs("sherpa",13,3000,"2000-ms"),100000]
info3000sherpa_13TeV_eta0_aftercuts = [info3000sherpalow_13TeV_eta0_aftercuts,info3000sherpamid_13TeV_eta0_aftercuts,info3000sherpahigh_13TeV_eta0_aftercuts]
hist3000sherpa_13TeV_eta0_aftercuts = dc.concatenate(info3000sherpa_13TeV_eta0_aftercuts,"hist3000sherpa_13TeV_eta0_aftercuts",LUMI)

info4000sherpalow_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hleadingPhoEta",findXs("sherpa",8,4000,"200-750"),100000]
info4000sherpamid_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hleadingPhoEta",findXs("sherpa",8,4000,"750-2000"),100000]
info4000sherpahigh_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hleadingPhoEta",findXs("sherpa",8,4000,"2000-ms"),100000]
info4000sherpa_8TeV_eta0_aftercuts = [info4000sherpalow_8TeV_eta0_aftercuts,info4000sherpamid_8TeV_eta0_aftercuts,info4000sherpahigh_8TeV_eta0_aftercuts]
hist4000sherpa_8TeV_eta0_aftercuts = dc.concatenate(info4000sherpa_8TeV_eta0_aftercuts,"hist4000sherpa_8TeV_eta0_aftercuts",LUMI)

info4000sherpalow_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hleadingPhoEta",findXs("sherpa",13,4000,"200-750"),100000]
info4000sherpamid_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hleadingPhoEta",findXs("sherpa",13,4000,"750-2000"),100000]
info4000sherpahigh_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hleadingPhoEta",findXs("sherpa",13,4000,"2000-ms"),100000]
info4000sherpa_13TeV_eta0_aftercuts = [info4000sherpalow_13TeV_eta0_aftercuts,info4000sherpamid_13TeV_eta0_aftercuts,info4000sherpahigh_13TeV_eta0_aftercuts]
hist4000sherpa_13TeV_eta0_aftercuts = dc.concatenate(info4000sherpa_13TeV_eta0_aftercuts,"hist4000sherpa_13TeV_eta0_aftercuts",LUMI)

info100000sherpalow_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hleadingPhoEta",findXs("sherpa",8,100000,"200-750"),100000]
info100000sherpamid_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hleadingPhoEta",findXs("sherpa",8,100000,"750-2000"),100000]
info100000sherpahigh_8TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hleadingPhoEta",findXs("sherpa",8,100000,"2000-ms"),100000]
info100000sherpa_8TeV_eta0_aftercuts = [info100000sherpalow_8TeV_eta0_aftercuts,info100000sherpamid_8TeV_eta0_aftercuts,info100000sherpahigh_8TeV_eta0_aftercuts]
hist100000sherpa_8TeV_eta0_aftercuts = dc.concatenate(info100000sherpa_8TeV_eta0_aftercuts,"hist100000sherpa_8TeV_eta0_aftercuts",LUMI)

info100000sherpalow_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hleadingPhoEta",findXs("sherpa",13,100000,"200-750"),100000]
info100000sherpamid_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hleadingPhoEta",findXs("sherpa",13,100000,"750-2000"),100000]
info100000sherpahigh_13TeV_eta0_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hleadingPhoEta",findXs("sherpa",13,100000,"2000-ms"),100000]
info100000sherpa_13TeV_eta0_aftercuts = [info100000sherpalow_13TeV_eta0_aftercuts,info100000sherpamid_13TeV_eta0_aftercuts,info100000sherpahigh_13TeV_eta0_aftercuts]
hist1000sherpa_13TeV_eta0_aftercuts = dc.concatenate(info100000sherpa_13TeV_eta0_aftercuts,"hist100000sherpa_13TeV_eta0_aftercuts",LUMI)

plotTwoHistos(hist3000p8_8TeV_eta0_aftercuts,"Pythia 8 (8 TeV)",hist3000sherpa_8TeV_eta0_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_eta0_aftercuts_ms3000.pdf",-6.,6.,False,"Leading Photon #eta",2)
plotTwoHistos(hist3000p8_13TeV_eta0_aftercuts,"Pythia 8 (13 TeV)",hist3000sherpa_13TeV_eta0_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_eta0_aftercuts_ms3000.pdf",-6.,6.,False,"Leading Photon #eta",2)

plotTwoHistos(hist4000p8_8TeV_eta0_aftercuts,"Pythia 8 (8 TeV)",hist4000sherpa_8TeV_eta0_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_eta0_aftercuts_ms4000.pdf",-6.,6.,False,"Leading Photon #eta",2)
plotTwoHistos(hist4000p8_13TeV_eta0_aftercuts,"Pythia 8 (13 TeV)",hist4000sherpa_13TeV_eta0_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_eta0_aftercuts_ms4000.pdf",-6.,6.,False,"Leading Photon #eta",2)

plotTwoHistos(hist100000p8_8TeV_eta0_aftercuts,"Pythia 8 (8 TeV)",hist100000sherpa_8TeV_eta0_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_eta0_aftercuts_ms100000.pdf",-6.,6.,False,"Leading Photon #eta",2)
plotTwoHistos(hist100000p8_13TeV_eta0_aftercuts,"Pythia 8 (13 TeV)",hist100000sherpa_13TeV_eta0_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_eta0_aftercuts_ms100000.pdf",-6.,6.,False,"Leading Photon #eta",2)

# subleading eta

info3000p8low_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat200-750.root","analyze/hsubleadingPhoEta",findXs("p8",8,3000,"200-750"),100000]
info3000p8mid_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat750-2000.root","analyze/hsubleadingPhoEta",findXs("p8",8,3000,"750-2000"),100000]
info3000p8high_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT3000_mHat2000-lt.root","analyze/hsubleadingPhoEta",findXs("p8",8,3000,"2000-lt"),100000]
info3000p8_8TeV_eta1_aftercuts = [info3000p8low_8TeV_eta1_aftercuts,info3000p8mid_8TeV_eta1_aftercuts,info3000p8high_8TeV_eta1_aftercuts]
hist3000p8_8TeV_eta1_aftercuts = dc.concatenate(info3000p8_8TeV_eta1_aftercuts,"hist3000p8_8TeV_eta1_aftercuts",LUMI)

info3000p8low_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat200-750.root","analyze/hsubleadingPhoEta",findXs("p8",13,3000,"200-750"),100000]
info3000p8mid_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat750-2000.root","analyze/hsubleadingPhoEta",findXs("p8",13,3000,"750-2000"),100000]
info3000p8high_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT3000_mHat2000-lt.root","analyze/hsubleadingPhoEta",findXs("p8",13,3000,"2000-lt"),100000]
info3000p8_13TeV_eta1_aftercuts = [info3000p8low_13TeV_eta1_aftercuts,info3000p8mid_13TeV_eta1_aftercuts,info3000p8high_13TeV_eta1_aftercuts]
hist3000p8_13TeV_eta1_aftercuts = dc.concatenate(info3000p8_13TeV_eta1_aftercuts,"hist3000p8_13TeV_eta1_aftercuts",LUMI)

info4000p8low_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat200-750.root","analyze/hsubleadingPhoEta",findXs("p8",8,4000,"200-750"),100000]
info4000p8mid_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat750-2000.root","analyze/hsubleadingPhoEta",findXs("p8",8,4000,"750-2000"),100000]
info4000p8high_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT4000_mHat2000-lt.root","analyze/hsubleadingPhoEta",findXs("p8",8,4000,"2000-lt"),100000]
info4000p8_8TeV_eta1_aftercuts = [info4000p8low_8TeV_eta1_aftercuts,info4000p8mid_8TeV_eta1_aftercuts,info4000p8high_8TeV_eta1_aftercuts]
hist4000p8_8TeV_eta1_aftercuts = dc.concatenate(info4000p8_8TeV_eta1_aftercuts,"hist4000p8_8TeV_eta1_aftercuts",LUMI)

info4000p8low_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat200-750.root","analyze/hsubleadingPhoEta",findXs("p8",13,4000,"200-750"),100000]
info4000p8mid_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat750-2000.root","analyze/hsubleadingPhoEta",findXs("p8",13,4000,"750-2000"),100000]
info4000p8high_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT4000_mHat2000-lt.root","analyze/hsubleadingPhoEta",findXs("p8",13,4000,"2000-lt"),100000]
info4000p8_13TeV_eta1_aftercuts = [info4000p8low_13TeV_eta1_aftercuts,info4000p8mid_13TeV_eta1_aftercuts,info4000p8high_13TeV_eta1_aftercuts]
hist4000p8_13TeV_eta1_aftercuts = dc.concatenate(info4000p8_13TeV_eta1_aftercuts,"hist4000p8_13TeV_eta1_aftercuts",LUMI)

info100000p8low_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat200-750.root","analyze/hsubleadingPhoEta",findXs("p8",8,100000,"200-750"),100000]
info100000p8mid_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat750-2000.root","analyze/hsubleadingPhoEta",findXs("p8",8,100000,"750-2000"),100000]
info100000p8high_8TeV_eta1_aftercuts = ["ADDdiPhoton_8TeV_LambdaT100000_mHat2000-lt.root","analyze/hsubleadingPhoEta",findXs("p8",8,100000,"2000-lt"),100000]
info100000p8_8TeV_eta1_aftercuts = [info100000p8low_8TeV_eta1_aftercuts,info100000p8mid_8TeV_eta1_aftercuts,info100000p8high_8TeV_eta1_aftercuts]
hist100000p8_8TeV_eta1_aftercuts = dc.concatenate(info100000p8_8TeV_eta1_aftercuts,"hist100000p8_8TeV_eta1_aftercuts",LUMI)

info100000p8low_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat200-750.root","analyze/hsubleadingPhoEta",findXs("p8",13,100000,"200-750"),100000]
info100000p8mid_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat750-2000.root","analyze/hsubleadingPhoEta",findXs("p8",13,100000,"750-2000"),100000]
info100000p8high_13TeV_eta1_aftercuts = ["ADDdiPhoton_13TeV_LambdaT100000_mHat2000-lt.root","analyze/hsubleadingPhoEta",findXs("p8",13,100000,"2000-lt"),100000]
info100000p8_13TeV_eta1_aftercuts = [info100000p8low_13TeV_eta1_aftercuts,info100000p8mid_13TeV_eta1_aftercuts,info100000p8high_13TeV_eta1_aftercuts]
hist100000p8_13TeV_eta1_aftercuts = dc.concatenate(info100000p8_13TeV_eta1_aftercuts,"hist100000p8_13TeV_eta1_aftercuts",LUMI)

# Sherpa

info3000sherpalow_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,3000,"200-750"),100000]
info3000sherpamid_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,3000,"750-2000"),100000]
info3000sherpahigh_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,3000,"2000-ms"),100000]
info3000sherpa_8TeV_eta1_aftercuts = [info3000sherpalow_8TeV_eta1_aftercuts,info3000sherpamid_8TeV_eta1_aftercuts,info3000sherpahigh_8TeV_eta1_aftercuts]
hist3000sherpa_8TeV_eta1_aftercuts = dc.concatenate(info3000sherpa_8TeV_eta1_aftercuts,"hist3000sherpa_8TeV_eta1_aftercuts",LUMI)

info3000sherpalow_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG200-750.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,3000,"200-750"),100000]
info3000sherpamid_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG750-2000.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,3000,"750-2000"),100000]
info3000sherpahigh_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS3000_MGG2000-ms.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,3000,"2000-ms"),100000]
info3000sherpa_13TeV_eta1_aftercuts = [info3000sherpalow_13TeV_eta1_aftercuts,info3000sherpamid_13TeV_eta1_aftercuts,info3000sherpahigh_13TeV_eta1_aftercuts]
hist3000sherpa_13TeV_eta1_aftercuts = dc.concatenate(info3000sherpa_13TeV_eta1_aftercuts,"hist3000sherpa_13TeV_eta1_aftercuts",LUMI)

info4000sherpalow_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,4000,"200-750"),100000]
info4000sherpamid_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,4000,"750-2000"),100000]
info4000sherpahigh_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,4000,"2000-ms"),100000]
info4000sherpa_8TeV_eta1_aftercuts = [info4000sherpalow_8TeV_eta1_aftercuts,info4000sherpamid_8TeV_eta1_aftercuts,info4000sherpahigh_8TeV_eta1_aftercuts]
hist4000sherpa_8TeV_eta1_aftercuts = dc.concatenate(info4000sherpa_8TeV_eta1_aftercuts,"hist4000sherpa_8TeV_eta1_aftercuts",LUMI)

info4000sherpalow_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG200-750.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,4000,"200-750"),100000]
info4000sherpamid_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG750-2000.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,4000,"750-2000"),100000]
info4000sherpahigh_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS4000_MGG2000-ms.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,4000,"2000-ms"),100000]
info4000sherpa_13TeV_eta1_aftercuts = [info4000sherpalow_13TeV_eta1_aftercuts,info4000sherpamid_13TeV_eta1_aftercuts,info4000sherpahigh_13TeV_eta1_aftercuts]
hist4000sherpa_13TeV_eta1_aftercuts = dc.concatenate(info4000sherpa_13TeV_eta1_aftercuts,"hist4000sherpa_13TeV_eta1_aftercuts",LUMI)

info100000sherpalow_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,100000,"200-750"),100000]
info100000sherpamid_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,100000,"750-2000"),100000]
info100000sherpahigh_8TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_8TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hsubleadingPhoEta",findXs("sherpa",8,100000,"2000-ms"),100000]
info100000sherpa_8TeV_eta1_aftercuts = [info100000sherpalow_8TeV_eta1_aftercuts,info100000sherpamid_8TeV_eta1_aftercuts,info100000sherpahigh_8TeV_eta1_aftercuts]
hist100000sherpa_8TeV_eta1_aftercuts = dc.concatenate(info100000sherpa_8TeV_eta1_aftercuts,"hist100000sherpa_8TeV_eta1_aftercuts",LUMI)

info100000sherpalow_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG200-750.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,100000,"200-750"),100000]
info100000sherpamid_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG750-2000.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,100000,"750-2000"),100000]
info100000sherpahigh_13TeV_eta1_aftercuts = ["ADDdiPhoton_sherpa_13TeV_KK1_NED4_MS100000_MGG2000-ms.root","analyze/hsubleadingPhoEta",findXs("sherpa",13,100000,"2000-ms"),100000]
info100000sherpa_13TeV_eta1_aftercuts = [info100000sherpalow_13TeV_eta1_aftercuts,info100000sherpamid_13TeV_eta1_aftercuts,info100000sherpahigh_13TeV_eta1_aftercuts]
hist1000sherpa_13TeV_eta1_aftercuts = dc.concatenate(info100000sherpa_13TeV_eta1_aftercuts,"hist100000sherpa_13TeV_eta1_aftercuts",LUMI)

plotTwoHistos(hist3000p8_8TeV_eta1_aftercuts,"Pythia 8 (8 TeV)",hist3000sherpa_8TeV_eta1_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_eta1_aftercuts_ms3000.pdf",-6.,6.,False,"Subleading Photon #eta",2)
plotTwoHistos(hist3000p8_13TeV_eta1_aftercuts,"Pythia 8 (13 TeV)",hist3000sherpa_13TeV_eta1_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_eta1_aftercuts_ms3000.pdf",-6.,6.,False,"Subleading Photon #eta",2)

plotTwoHistos(hist4000p8_8TeV_eta1_aftercuts,"Pythia 8 (8 TeV)",hist4000sherpa_8TeV_eta1_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_eta1_aftercuts_ms4000.pdf",-6.,6.,False,"Subleading Photon #eta",2)
plotTwoHistos(hist4000p8_13TeV_eta1_aftercuts,"Pythia 8 (13 TeV)",hist4000sherpa_13TeV_eta1_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_eta1_aftercuts_ms4000.pdf",-6.,6.,False,"Subleading Photon #eta",2)

plotTwoHistos(hist100000p8_8TeV_eta1_aftercuts,"Pythia 8 (8 TeV)",hist100000sherpa_8TeV_eta1_aftercuts,"Sherpa (8 TeV)","p8sherpacomp_8TeV_eta1_aftercuts_ms100000.pdf",-6.,6.,False,"Subleading Photon #eta",2)
plotTwoHistos(hist100000p8_13TeV_eta1_aftercuts,"Pythia 8 (13 TeV)",hist100000sherpa_13TeV_eta1_aftercuts,"Sherpa (13 TeV)","p8sherpacomp_13TeV_eta1_aftercuts_ms100000.pdf",-6.,6.,False,"Subleading Photon #eta",2)


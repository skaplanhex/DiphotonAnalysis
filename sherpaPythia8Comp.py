print "loading ROOT..."
from ROOT import *
import sys
print "done."

gROOT.SetBatch()
gStyle.SetOptStat(0)

sherpaXSs={}
pythia8XSs = {}

xsFile = open("xsections_p8sherpacomparison.txt",'r')

for line in xsFile:
    s = line.split()
    genName = str(s[0])
    if genName == "p8":
        pythia8XSs[ (int(s[1]),s[2]) ] = float(s[-1]) #key is a tuple (MS,pTHatBin)
    elif genName == "sherpa":
        sherpaXSs[ (int(s[1]),s[2]) ] = float(s[-1])  #key is a tuple (MS,pTHatBin)
    else:
        print "Generator name not recognized, what's going on?"
        sys.exit(1)
xsFile.close()

# define background cross sections and histograms

LUMI = 1. #fb**-1
NEVENTS=1.e5

p8BkgXS_lowpt = pythia8XSs[(100000,"150-500")] 
p8BkgXS_highpt = pythia8XSs[(100000,"500-Inf")]

sherpaBkgXS_lowpt = sherpaXSs[(100000,"150-500")]
sherpaBkgXS_highpt = sherpaXSs[(100000,"500-Inf")]

p8BkgFile_lowpt = TFile("plots_hewett1_LambdaT100000_pTHat150-500.root","read")
p8BkgFile_highpt = TFile("plots_hewett1_LambdaT100000_pTHat500-Inf.root","read")

sherpaBkgFile_lowpt = TFile("plots_sherpa_Ms100000_Mgg300-1000.root","read")
sherpaBkgFile_highpt = TFile("plots_sherpa_Ms100000_Mgg1000-Inf.root","read")

p8BkgHist_lowpt = p8BkgFile_lowpt.Get("analyze/hggMass")
p8BkgHist_lowpt.Sumw2()
p8BkgHist_lowpt.Scale( (p8BkgXS_lowpt/NEVENTS)*LUMI )

p8BkgHist_highpt = p8BkgFile_highpt.Get("analyze/hggMass")
p8BkgHist_highpt.Sumw2()
p8BkgHist_highpt.Scale( (p8BkgXS_highpt/NEVENTS)*LUMI )

sherpaBkgHist_lowpt = sherpaBkgFile_lowpt.Get("analyze/hggMass")
sherpaBkgHist_lowpt.Sumw2()
sherpaBkgHist_lowpt.Scale( (sherpaBkgXS_lowpt/NEVENTS)*LUMI )

sherpaBkgHist_highpt = sherpaBkgFile_highpt.Get("analyze/hggMass")
sherpaBkgHist_highpt.Sumw2()
sherpaBkgHist_highpt.Scale( (sherpaBkgXS_highpt/NEVENTS)*LUMI )

for ms in (3000,5000):
    p8SigFile_lowpt = TFile("plots_hewett1_LambdaT%i_pTHat150-500.root"%(ms),"read")
    p8SigFile_highpt = TFile("plots_hewett1_LambdaT%i_pTHat500-Inf.root"%(ms),"read")

    sherpaSigFile_lowpt = TFile("plots_sherpa_Ms%i_Mgg300-1000.root"%(ms),"read")
    sherpaSigFile_highpt = TFile("plots_sherpa_Ms%i_Mgg1000-Inf.root"%(ms),"read")

    p8XS_lowpt = pythia8XSs[(ms,"150-500")]
    p8XS_highpt = pythia8XSs[(ms,"500-Inf")]

    sherpaXS_lowpt = sherpaXSs[(ms,"150-500")]
    sherpaXS_highpt = sherpaXSs[(ms,"500-Inf")]

    # get and scale all the histograms
    p8Hist_lowpt = p8SigFile_lowpt.Get("analyze/hggMass")
    p8Hist_lowpt.Sumw2()
    p8Hist_lowpt.Scale( (p8XS_lowpt/NEVENTS)*LUMI )

    p8Hist_highpt = p8SigFile_highpt.Get("analyze/hggMass")
    p8Hist_highpt.Sumw2()
    p8Hist_highpt.Scale( (p8XS_highpt/NEVENTS)*LUMI )

    sherpaHist_lowpt = sherpaSigFile_lowpt.Get("analyze/hggMass")
    sherpaHist_lowpt.Sumw2()
    sherpaHist_lowpt.Scale( (sherpaXS_lowpt/NEVENTS)*LUMI )

    sherpaHist_highpt = sherpaSigFile_highpt.Get("analyze/hggMass")
    sherpaHist_highpt.Sumw2()
    sherpaHist_highpt.Scale( (sherpaXS_highpt/NEVENTS)*LUMI )

    # combine pT bins into one histogram

    p8Hist = p8Hist_lowpt.Clone()
    p8Hist.Add(p8Hist_highpt,1.)

    sherpaHist = sherpaHist_lowpt.Clone()
    sherpaHist.Add(sherpaHist_highpt,1.)

    p8Hist_bkg = p8BkgHist_lowpt.Clone()
    p8Hist_bkg.Add(p8BkgHist_highpt,1.)

    sherpaHist_bkg = sherpaBkgHist_lowpt.Clone()
    sherpaHist_bkg.Add(sherpaBkgHist_highpt,1.)

    # now subtract the background to get a signal only plot

    p8Hist_sig = p8Hist.Clone()
    p8Hist_sig.Add(p8Hist_bkg,-1.)

    sherpaHist_sig = sherpaHist.Clone()
    sherpaHist_sig.Add(sherpaHist_bkg,-1.)

    # now that we finally have the histograms, make plots!

    c = TCanvas("c","",800,800)

    p8Hist.SetLineColor(kBlack)
    p8Hist.SetLineWidth(2)
    sherpaHist.SetLineColor(kRed)
    sherpaHist.SetLineWidth(2)
    sherpaHist.SetLineStyle(4)

    p8Hist.Draw()
    sherpaHist.Draw("same")

    leg = TLegend(.63,.37,.87,.48)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.02)
    leg.AddEntry(p8Hist,"Pythia 8","L")
    leg.AddEntry(sherpaHist,"Sherpa","L")
    leg.Draw()

    # l1 = TLatex()
    # l1.SetTextAlign(13)
    # l1.SetTextFont(42)
    # l1.SetTextSize(0.025)
    # l1.DrawLatex(0.63,0.57,"testing")

    c.SaveAs("p8sherpacomp_sigbkg_ms%i.pdf"%ms)

    c.Clear()

    p8Hist_sig.SetLineColor(kBlack)
    p8Hist_sig.SetLineWidth(2)
    sherpaHist_sig.SetLineColor(kRed)
    sherpaHist_sig.SetLineWidth(2)
    sherpaHist_sig.SetLineStyle(4)

    p8Hist_sig2 = p8Hist_sig.Clone()
    sherpaHist_sig2 = sherpaHist_sig.Clone()
    p8Hist_sig2.Rebin(2)
    sherpaHist_sig2.Rebin(2)

    sherpaHist_sig2.Draw()
    p8Hist_sig2.Draw("same")

    leg = TLegend(.63,.37,.87,.48)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.02)
    leg.AddEntry(p8Hist_sig2,"Pythia 8","L")
    leg.AddEntry(sherpaHist_sig2,"Sherpa","L")
    leg.Draw()

    c.SaveAs("p8sherpacomp_sig_ms%i.pdf"%ms)

    c.Clear()

    p8Hist_bkg.SetLineColor(kBlue)
    p8Hist_bkg.SetLineWidth(2)
    p8Hist_bkg.SetLineStyle(4)

    p8Hist_bkg.Draw()
    p8Hist.Draw("same")

    leg = TLegend(.63,.77,.87,.88)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.02)
    leg.AddEntry(p8Hist,"ADD S+B (Pythia 8)","L")
    leg.AddEntry(p8Hist_bkg,"SM Background (Pythia 8)","L")
    leg.Draw()

    c.SetLogy()
    c.SaveAs("p8sherpacomp_p8_ms%i.pdf"%ms)

    c.Clear()

    sherpaHist_bkg.SetLineColor(kBlue)
    sherpaHist_bkg.SetLineWidth(2)
    sherpaHist_bkg.SetLineStyle(4)

    sherpaHist.SetLineStyle(0)
    sherpaHist.SetLineColor(kBlack)

    sherpaHist_bkg.Draw()
    sherpaHist.Draw("same")

    leg = TLegend(.63,.77,.87,.88)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.02)
    leg.AddEntry(sherpaHist,"ADD S+B (Sherpa)","L")
    leg.AddEntry(sherpaHist_bkg,"SM Background (Sherpa)","L")
    leg.Draw()

    c.SetLogy()
    c.SaveAs("p8sherpacomp_sherpa_ms%i.pdf"%ms)

    c.Clear()

    p8Hist_bkg.SetLineColor(kBlack)
    sherpaHist_bkg.SetLineColor(kRed)

    sherpaHist_bkg.Draw()
    p8Hist_bkg.Draw("same")

    leg = TLegend(.63,.77,.87,.88)
    leg.SetBorderSize(0)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(42)
    leg.SetTextSize(0.02)
    leg.AddEntry(p8Hist_bkg,"SM Background (Pythia 8)","L")
    leg.AddEntry(sherpaHist_bkg,"SM Background (Sherpa)","L")
    leg.Draw()

    c.SaveAs("p8sherpacomp_bkg_ms%s.pdf"%ms)

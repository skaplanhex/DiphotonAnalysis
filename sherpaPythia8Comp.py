print "loading ROOT..."
from ROOT import *
# from numpy import *
print "done."

gROOT.SetBatch()

# Xss
sherpaXSs={} #already in fb
# sherpaXSs[2000] = 703.788
# sherpaXSs[4000] = 81.7988
sherpaXSs[2000] = 3013.64
sherpaXSs[4000] = 95.2424
sherpaXSs[100000] = 360.707

pythia8XSs = {} # given initially in mb but converted here
pythia8XSs[2000] = (1.603450e-09)*(1e12)
pythia8XSs[4000] = (5.606350e-12)*(1e12)
pythia8XSs[100000] = (1.636800e-12)*(1e12)

# sherpaFilenames={
#     "low":"sherpabkg_mgg300-1000.root",
#     "hi":"sherpabkg_mgg1000-Inf.root"
# }
# pythiaFilenames={
#     "low":"plots_LambdaTStudy_LambdaT100K_pTHat150-500.root",
#     "hi":"plots_LambdaTStudy_LambdaT100K_pTHat500-Inf.root"
# }

for ms in (2000,4000):
    sherpaFile = TFile("sherpa_himass_Ms%i_MCut8600_plots.root"%ms,"read")
    pythia8File = TFile("/uscms_data/d3/skaplan/diphotons/CMSSW_7_1_1/src/Analyzers/DiphotonAnalyzer/plots_LambdaTStudy_LambdaT%i_pTHat500-Inf.root"%ms,"read")

    LUMI = 1. #fb**-1

    sherpaXS = sherpaXSs[ms]
    pythiaXS = pythia8XSs[ms]

    sherpaHist = sherpaFile.Get("analyze/hggMass")
    pythiaHist = pythia8File.Get("analyze/hggMass")

    sherpaNEvents=100000.
    pythiaNEvents=100000.

    sherpaHist.Scale( (sherpaXS/sherpaNEvents)*LUMI )
    pythiaHist.Scale( (pythiaXS/pythiaNEvents)*LUMI )

    sherpaHist.SetLineColor(kRed+1)
    sherpaHist.SetLineStyle(4)
    sherpaHist.SetLineWidth(2)

    pythiaHist.SetLineColor(kBlack)
    # pythiaHist.SetLineStyle(4)
    pythiaHist.SetLineWidth(2)

    c = TCanvas("c","",800,800)

    sherpaHist.GetXaxis().SetTitle("M_{#gamma#gamma} (GeV/c^{2})")
    sherpaHist.GetYaxis().SetTitle("Number of Events")
    sherpaHist.Draw()
    pythiaHist.Draw("same")

    c.SaveAs("sherpaPythia8Comp_Ms%i_MCut8600_plots.pdf"%ms)

    # raw_input("Enter to quit: ")





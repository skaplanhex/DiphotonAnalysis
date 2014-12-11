print "loading ROOT..."
from ROOT import *
# from numpy import *
print "done."

# gROOT.SetBatch()

# XSs in fb
sherpaXSs={
    "low":(5.09574*(1.e3)),
    "hi":(0.0652723*(1.e3))
}

pythiaXSs={
    "low":(1.725150e-10)*(1e12),
    "hi":(1.636800e-12)*(1e12)
}

sherpaFilenames={
    "low":"sherpabkg_mgg300-1000.root",
    "hi":"sherpabkg_mgg1000-Inf.root"
}
pythiaFilenames={
    "low":"plots_LambdaTStudy_LambdaT100K_pTHat150-500.root",
    "hi":"plots_LambdaTStudy_LambdaT100K_pTHat500-Inf.root"
}

# xsbkg150=(1.725150e-10)*(1e12)
# xsbkg500=(1.636800e-12)*(1e12)
LUMI = 1. #fb**-1

# for pt in ("low",):

pt = "hi"
sherpaXS = sherpaXSs[pt]
pythiaXS = pythiaXSs[pt]

sherpaFile = TFile(sherpaFilenames[pt],"read")
pythiaFile = TFile(pythiaFilenames[pt],"read")

sherpaHist = sherpaFile.Get("analyze/hggMass")
pythiaHist = pythiaFile.Get("analyze/hggMass")

sherpaNEvents=10000.
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

raw_input("Enter to quit: ")





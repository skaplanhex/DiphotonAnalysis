from ROOT import *

gROOT.SetBatch()

fbkg = TFile('plots_LambdaTStudy_LambdaT100K_pTHat150-500.root',"read")
hbkg = fbkg.Get("analyze/hggMass")
hbkg.GetXaxis().SetRangeUser(0,1600)
hbkg.SetLineColor(kRed+1)
hbkg.SetLineWidth(2)
hbkg.SetLineStyle(4)
hbkg.Sumw2()

for lt in ("2000","3000","3500","4000","4500","5000","6000"):
    fsigbkg = TFile("plots_LambdaTStudy_LambdaT%s_pTHat150-500.root"%lt,"READ")
    hsigbkg = fsigbkg.Get("analyze/hggMass")
    hsigbkg.GetXaxis().SetRangeUser(0,1600)
    hsigbkg.SetLineWidth(2)
    hsigbkg.SetLineColor(kBlack)
    c = TCanvas()
    hsigbkg.GetXaxis().SetTitle("M_{#gamma#gamma} (GeV)")
    hsigbkg.Sumw2()
    hsigbkg.Draw()
    hbkg.Draw("same")
    c.SetLogy()
    c.SaveAs("inputDists_LambdaT%s.png"%lt)
print "loading ROOT..."
from ROOT import *
# from numpy import *
print "done."

xsbkg=3.697e-10
xssigplusbkg=1.977e-09
xssig = xssigplusbkg-xsbkg

freg = TFile("plots_N2_MD2000_RUN2.root","READ")
finf = TFile("plots_N2_MD2000_LambdaT100K_2.root","READ")

hreg = freg.Get("analyze/hggMass")
hinf = finf.Get("analyze/hggMass")

# hregcopy = hreg.Clone()
# hinfcopy = hinf.Clone()

# # hsig = xssigbkg*hreg - xsbkg*hinf
# hsig = hreg.Clone()
# hsig.Scale(xssigplusbkg)
# hsig.Add(hinfcopy,-1.*xsbkg)

sigbkgint = float(hreg.Integral())
bkgint = float(hreg.Integral())

# hreg.Scale(823./171.)


hreg.Scale(xssigplusbkg/sigbkgint)
hinf.Scale(xsbkg/bkgint)
# hreg.Scale(xssigplusbkg)
# hinf.Scale(xsbkg)

hsig=hreg.Clone()
hsig.Add(hinf,-1.)

# for h in (hreg,hinf):
#     h.Scale( 1./h.Integral() )

c = TCanvas("c","",1000,800)
c.Divide(1,2)
pad1 = c.cd(1)
hreg.SetLineColor(kBlack)
hinf.SetLineColor(kRed+1)
hinf.SetLineStyle(4)
for h in (hreg,hinf):
    h.SetLineWidth(2)
# hreg.GetYaxis().SetRangeUser(0,1000)
hreg.Draw()
hinf.Draw("same")
leg = pad1.BuildLegend()
pad1.SetLogy()

# calculate peak heights
# regHeights=[]
# infHeights=[]
# for i in range(hreg.GetNbinsX()):
#     regHeights.append(hreg.GetBinContent(i))
#     infHeights.append(hinf.GetBinContent(i))
# regHeights = array(regHeights)
# infHeights = array(infHeights)

# print "bkg max = %.2f"%(infHeights.max())
# print "sig + bkg max = %.2f"%(regHeights.max())


# pad1.SetLogy()
c.cd(2)
# hsig.SetTitle("(#LambdaT=2000) - (#LambdaT=#infty)")
hsig.GetYaxis().SetTitle("(#Lambda_{T}=2000) - (#Lambda_{T}=#infty)")
hsig.Scale(xssig/hsig.Integral())
# hsig.GetYaxis().SetRangeUser(-0.01,0.01)
hsig.Draw()

# c2 = TCanvas()
# c2.cd()

# hsig.SetTitle("(#LambdaT=2000) - (#LambdaT=#infty)")
# hsig.GetYaxis().SetRangeUser(-0.01,0.01)
# hsig.Draw()
raw_input("Enter to quit: ")

freg.Close()
finf.Close()
print "loading ROOT and numpy..."
from ROOT import *
from numpy import *
print "done."

gROOT.SetBatch()
#this is a constant 
xsbkg=(3.697e-10)*(1e12) # convert to fb
LUMI = 1. #fb**-1

#build cross section dictionary
f = open('xsections_lambdaTstudy.txt','r')
xsdict={}
for line in f:
    s = line.split()
    xsdict[ int( s[0] ) ]= float( s[1] )*(1e12) # convert to fb
f.close()

#loop over lambdaTs
for lt in arange(0,10500,500)[1:]: #[500,1000,...,9500,10000]
    # if lt != 2000:
    #     continue
    xssigplusbkg = xsdict[lt]
    xssig = xssigplusbkg-xsbkg
    if xssig <=0: #not sure how to deal with this yet.
        continue

    freg = TFile("plots_LambdaTstudy_LambdaT%i.root"%lt,"READ")
    finf = TFile("plots_N2_MD2000_LambdaT100K_2.root","READ")

    hreg = freg.Get("analyze/hggMass")
    hinf = finf.Get("analyze/hggMass")

    hreg.Sumw2()
    hinf.Sumw2()

    hreg.Rebin(4)
    hinf.Rebin(4)

    # hregcopy = hreg.Clone()
    # hinfcopy = hinf.Clone()

    # # hsig = xssigbkg*hreg - xsbkg*hinf
    # hsig = hreg.Clone()
    # hsig.Scale(xssigplusbkg)
    # hsig.Add(hinfcopy,-1.*xsbkg)

    # sigbkgint = float( hreg.Integral(0,hreg.GetNbinsX()+1) )
    # bkgint = float( hinf.Integral(0,hinf.GetNbinsX()+1) )

    #luminosity is 1 fb**-1
    NEVENTS=10000.
    hreg.Scale( (xssigplusbkg/NEVENTS)*LUMI )
    hinf.Scale( (xsbkg/NEVENTS)*LUMI )
    # hreg.Scale(xssigplusbkg)
    # hinf.Scale(xsbkg)

    hsig=hreg.Clone()
    hsig.Add(hinf,-1.)

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
    hsig.SetTitle("(#LambdaT=%i) - (#LambdaT=#infty)"%lt)
    hsig.GetYaxis().SetTitle("(#Lambda_{T}=%i) - (#Lambda_{T}=#infty)"%lt)
    # print xssig
    hsig.Scale(xssig/hsig.Integral()*LUMI)
    # hsig.GetYaxis().SetRangeUser(-0.01,0.01)
    hsig.Draw()
    
    # integral plot of background
    c.cd(3)
    print hinf.Integral()
    hbkgint = hinf.Clone()
    hbkgint.SetName("hbkgint")
    hbkgint.SetTitle("")
    endBin = hinf.GetNbinsX()+1
    for i in range( 1, endBin):
        x = hinf.Integral(i,endBin)
        hbkgint.SetBinContent(i,x)
    hbkgint.Draw()

    c.SaveAs("massplot_LambdaT%i.png"%lt)
    freg.Close()
    finf.Close()

# c2 = TCanvas()
# c2.cd()

# hsig.SetTitle("(#LambdaT=2000) - (#LambdaT=#infty)")
# hsig.GetYaxis().SetRangeUser(-0.01,0.01)
# hsig.Draw()
# raw_input("Enter to quit: ")
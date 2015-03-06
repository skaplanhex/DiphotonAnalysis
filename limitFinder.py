def inBounds(testCase,integral,error):
    lowerBound = integral - error
    upperBound = integral + error

    if ( (testCase >= lowerBound) and (testCase <= upperBound) ):
        return True
    else:
        return False 

print "importing ROOT and numpy..."
from ROOT import *
import numpy as np
print "done."

# gROOT.SetBatch()

qqFilename = "gamma2MC_output/gamma2MC_mgg_qq_cteq6l1_r04_chiR05_chiF05_chiFR05_finebinning_NLO.out"
ggFilename = "gamma2MC_output/gamma2MC_mgg_gg_cteq6l1_r04_chiR05_chiF05_chiFR05_finebinning_NLO.out"

qqFile = open(qqFilename,'r')
ggFile = open(ggFilename,'r')

qqHist = TH1D("qqHist","",860,0,8600)
ggHist = TH1D("ggHist","",860,0,8600)

nloXS = 0
atDist = False

for line in qqFile:
    s = line.split()
    if len(s) < 1:
        continue
    if s[0]=='cross':
        nloXS = float( s[3] )
    elif s[0]=='M_gamgam':
        atDist = True
    elif atDist:
        mgg = float( s[0] )
        sigma = float( s[1] ) * 10.
        err = float( s[2] ) * 10.
        binNum = qqHist.Fill( mgg,sigma )
        qqHist.SetBinError(binNum,err)
qqFile.close()

nloXS = 0
atDist = False

for line in ggFile:
    s = line.split()
    if len(s) < 1:
        continue
    if s[0]=='cross':
        nloXS = float( s[3] )
    elif s[0]=='M_gamgam':
        atDist = True
    elif atDist:
        mgg = float( s[0] )
        sigma = float( s[1] ) * 10.
        err = float( s[2] ) * 10.
        binNum = ggHist.Fill( mgg,sigma )
        ggHist.SetBinError(binNum,err)
ggFile.close()

# at this point, the histograms are filled.  The bin height is the total cross section in fb in that mass bin.  Now, scale to 10/fb

qqHist.Scale(10.)
ggHist.Scale(10.)

#combine all diagrams into one histogram, nloHist
nloHist = qqHist.Clone()
nloHist.Add(ggHist,1.)

# c = TCanvas("c","",800,800)
# c.SetLogy()
# nloHist.SetLineColor(kRed)
# nloHist.Draw()
# raw_input("enter to quit: ")

# now calculate the bin boundaries

binLeftEdges = []
integralToInf = []
errors = []

nbins = nloHist.GetNbinsX()

# set bounds negative initially so they are only set once
bound100 = -10.
bound10 = -10.
bound1 = -10.
bound01 = -10.
bound001 = -10.
for iBin in range(nbins+1):
    # first calculate the integral and the associated error manually because pyroot is a PITA
    errsqu = 0
    integral = 0
    for i in range(iBin,nbins+1):
        errsqu += ( nloHist.GetBinError(i) )**2.
        integral += nloHist.GetBinContent(i)

    binLeftEdge = nloHist.GetBinLowEdge(iBin)
    error = np.sqrt(errsqu)

    binLeftEdges.append( binLeftEdge )
    integralToInf.append( integral )
    errors.append( error )

    # now test for the bounds
    if ( (inBounds(100.,integral,error)) and (bound100 < 0.) ):
        bound100 = binLeftEdge
    elif ( (inBounds(10.,integral,error)) and (bound10 < 0.) ):
        bound10 = binLeftEdge
    elif ( (inBounds(1.,integral,error)) and (bound1 < 0.) ):
        bound1 = binLeftEdge
    elif ( (inBounds(0.1,integral,error)) and (bound01 < 0.) ):
        bound01 = binLeftEdge
    elif ( (inBounds(0.01,integral,error)) and (bound001 < 0.) ):
        bound001 = binLeftEdge


binLeftEdges = np.array(binLeftEdges)
integralToInf = np.array(integralToInf)
errors = np.array(errors)

nloIntegral = TGraphErrors(len(binLeftEdges),binLeftEdges,integralToInf,np.zeros( len(binLeftEdges) ),errors)
nloIntegral.SetTitle("")
nloIntegral.GetXaxis().SetTitle("M_{#gamma#gamma} (GeV/c^{2})")
nloIntegral.GetYaxis().SetTitle("Number of Events with M_{#gamma#gamma} #geq Current M_{#gamma#gamma} Bin")
nloIntegral.GetYaxis().SetTitleOffset(1.4)

print "Bounds were found to be as follows for 10/fb :"
print "100 events: %.1f GeV"%bound100
print "10 events: %.1f GeV"%bound10
print "1 event: %.1f GeV"%bound1
print "0.1 events: %.1f GeV"%bound01
print "0.01 events: %.1f GeV"%bound001

c = TCanvas("c","",800,800)
c.SetLogy()
nloIntegral.Draw("AL")
raw_input("enter to quit: ")









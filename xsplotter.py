print "Importing ROOT and numpy..."
from ROOT import *
from numpy import *
print "done."

f = open('xsections_lambdaTstudy.txt','r')

lambdats = arange(500,10500,500)
xsecs = []
errors = []
for line in f:
    s = line.split()
    xsecs.append(float(s[1]))
    errors.append(float(s[2]))
c = TCanvas("c","",1000,800)
g = TGraphErrors(len(lambdats))
for i in range(len(lambdats)):
    g.SetPoint(i,lambdats[i],xsecs[i])
    g.SetPointError(i,0.,errors[i])
g.SetTitle("")
g.GetXaxis().SetTitle("#Lambda_{T} (GeV)")
g.GetYaxis().SetTitle("#sigma_{total} (mb)")
g.SetMarkerStyle(6)
c.SetLogy()
g.Draw("ACP")
raw_input("Enter to quit: ")
f.close()
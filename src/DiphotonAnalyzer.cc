// -*- C++ -*-
//
// Package:    ExampleAnalyzer
// Class:      ExampleAnalyzer
// 
/**\class ExampleAnalyzer ExampleAnalyzer.cc Analyzers/ExampleAnalyzer/src/ExampleAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  steven kaplan
//         Created:  Mon Mar 17 13:26:43 CDT 2014
// $Id$
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

//you need the TFileService in order to make plots
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
//for reco::Candidate
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CandidateFwd.h"
//for the GenParticleCollection and GenParticles
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/HepMCCandidate/interface/GenParticleFwd.h"
#include <vector>
#include "TLorentzVector.h"
#include "TH2D.h"
#include "TTree.h"
//
// class declaration
//

class DiphotonAnalyzer : public edm::EDAnalyzer {
   public:
      explicit DiphotonAnalyzer(const edm::ParameterSet&);
      ~DiphotonAnalyzer();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob();
      virtual bool isActualDecayProduct(int);
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      virtual void endRun(edm::Run const&, edm::EventSetup const&);
      virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------
      //the TFileService object
      edm::Service<TFileService> fs;
      //the handle which will be holding the genParticles from the event.  Don't confuse this with the particles InputTag!  These are two different things.  reco::GenParticleCollection is just a typedef for std::vector< reco::GenParticle >.
      edm::Handle< reco::GenParticleCollection > particles;
      //this object represents the InputTag that is passed to the analyzer in the config file
      edm::InputTag particles_;

      TH1D* hNumPhotons;
      TH1D* hggMass;
      TH1D* hggMass_varBinning;
      TH1D* hleadingPhoPt;
      TH1D* hleadingPhoEta;
      TH1D* hleadingPhoPhi;
      TH1D* hsubleadingPhoPt;
      TH1D* hsubleadingPhoEta;
      TH1D* hsubleadingPhoPhi;
      TH1D* hggDPhi;

      TH1D* allPhotonPt;
      TH1D* allPhotonEta;
      TH1D* allPhotonPhi;

      TH1D* hleadingPhoPt_beforecuts;
      TH1D* hleadingPhoEta_beforecuts;
      TH1D* hleadingPhoPhi_beforecuts;
      TH1D* hsubleadingPhoPt_beforecuts;
      TH1D* hsubleadingPhoEta_beforecuts;
      TH1D* hsubleadingPhoPhi_beforecuts;

      TH2D* subleadingPt_leadingPt;
      TH2D* leadingPt_mgg;
      TH2D* subleadingPt_mgg;
      TH2D* dRgg_mgg;
      TH2D* dEtagg_mgg;
      TH2D* dPhigg_mgg;

      bool leptonMode;
      bool makeTree;
      double leadingPtCut;
      double subleadingPtCut;
      int  numElectrons = 0;
      int  numMuons = 0;

      int numTotalEvents = 0;
      int numEventsPassingCuts = 0;

      std::string eventSource;

      // tree stuff
      TTree* tree;
      std::vector<double> PhotonPt;
      std::vector<double> PhotonEta;
      std::vector<double> PhotonPhi;
      std::vector<double> PhotonEnergy;
      std::vector<int> pdgId;
      std::vector<int> mother1;
      std::vector<int> mother2;
      std::vector<double> GenPt;
      std::vector<double> GenEta;
      std::vector<double> GenPhi;
      std::vector<double> GenEnergy;
      Double_t massHolder;
};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
DiphotonAnalyzer::DiphotonAnalyzer(const edm::ParameterSet& iConfig)

{
  //This line looks at the paramater set that is passed to the analyzer via the config file.  The particles_ object will represent whatever is passed to the particles variable in the config file (in our case, the genParticles).
  particles_ = iConfig.getParameter<edm::InputTag>("particles");
  leptonMode = ( iConfig.exists("leptonMode") ? iConfig.getParameter<bool>("leptonMode") : false );
  leadingPtCut = iConfig.getParameter<double>("leadingPtCut");
  subleadingPtCut = iConfig.getParameter<double>("subleadingPtCut");
  eventSource = iConfig.getParameter<std::string>("eventSource");
  makeTree = iConfig.getParameter<bool>("makeTree");
  std::cout << "eventSource: " << eventSource << std::endl;

}


DiphotonAnalyzer::~DiphotonAnalyzer()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

bool DiphotonAnalyzer::isActualDecayProduct(int pdgId){
  //take the absolute value just in case
  pdgId = abs(pdgId);
  if ( !leptonMode && pdgId == 22 ) return true;
  else if ( leptonMode && ((pdgId == 11) || (pdgId == 13)) ) return true;
  else return false;
}

// ------------ method called for each event  ------------
void
DiphotonAnalyzer::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
    using namespace edm;
    using namespace std;
    // unsigned int event = iEvent.id().event();
    // bool isSpecialEvent = (event == 191 || event == 265 || event == 348 || event == 641 || event == 771 || event == 952);
    // if ( !isSpecialEvent ) return;
    //particles_ is the InputTag object.  Look at the constructor for how it was initialized.  This line says to look in the event for the object with the InputTag that particles_ represents (in our case, the genParticles) and copy the content to the particles edm::Handle.  We can then do whatever we want with the particles!
    iEvent.getByLabel(particles_,particles);

    double leadingPhotonPt = -1.;
    double leadingPhotonEta = -1.;
    double leadingPhotonPhi = -1.;
    double leadingPhotonE = -1;
    double subleadingPhotonPt = -2.;
    double subleadingPhotonEta = -2.;
    double subleadingPhotonPhi = -2.;
    double subleadingPhotonE = -2.;
    int    numPhotons = 0;
    int    numFinalState = 0;

    numTotalEvents++;

    for (reco::GenParticleCollection::const_iterator iParticle = particles->begin(); iParticle != particles->end(); ++iParticle){

        int pdgIdNum = iParticle->pdgId();
        // if ( !isActualDecayProduct(pdgId) ) continue;
        // if ( pdgId != 22 ) continue;
        double pt = iParticle->pt();
        double eta = iParticle->eta();
        double phi = iParticle->phi();
        double energy = iParticle->energy();
        int status = iParticle->status();

        if (status == 1 && pdgIdNum==22){
          allPhotonPt->Fill(pt);
          allPhotonEta->Fill(eta);
          allPhotonPhi->Fill(phi);
        }

        //eta, pt, and status cuts
        if (status != 1) continue;

        // record all status 1 genparticles
        pdgId.push_back(pdgIdNum);
        // mother1.push_back();
        // mother2.push_back();
        GenPt.push_back(pt);
        GenEta.push_back(eta);
        GenPhi.push_back(phi);
        GenEnergy.push_back(energy);

        numFinalState++;

        if (pdgIdNum==22) numPhotons++;
        // else if (pdgId==11) numElectrons++;
        // else if (pdgId==13) numMuons++;

        if (pt > leadingPhotonPt){
            //if we found a new leading photon, then the new subleading is the previous leading
            // cout << "Found new leading photon!" << endl;
            // cout << "SUBLEADING PHOTON: Replacing " << subleadingPhotonPt << " with " << leadingPhotonPt << endl;
            subleadingPhotonPt = leadingPhotonPt;
            subleadingPhotonEta = leadingPhotonEta;
            subleadingPhotonPhi = leadingPhotonPhi;
            subleadingPhotonE = leadingPhotonE;

            // cout << "LEADING PHOTON: Replacing " << leadingPhotonPt << " with " << pt << endl;
            // cout << "" << endl;
            leadingPhotonPt = pt;
            leadingPhotonEta = eta;
            leadingPhotonPhi = phi;
            leadingPhotonE = energy;
        }
        else if ( (pt < leadingPhotonPt) && (pt > subleadingPhotonPt) ){
            //found a new subleading photon, keep leading photon as is but change the subleading to the new photon
            // cout << "Found new subleading photon!" << endl;
            // cout << "SUBLEADING PHOTON: Replacing " << subleadingPhotonPt << " with " << pt << endl;
            subleadingPhotonPt = pt;
            subleadingPhotonEta = eta;
            subleadingPhotonPhi = phi;
            subleadingPhotonE = energy;

        }

    } //end particle loop

    hNumPhotons->Fill(numPhotons);

    if (numFinalState >= 2){
      
      hleadingPhoPt_beforecuts->Fill(leadingPhotonPt);
      hleadingPhoEta_beforecuts->Fill(leadingPhotonEta);
      hleadingPhoPhi_beforecuts->Fill(leadingPhotonPhi);

      hsubleadingPhoPt_beforecuts->Fill(subleadingPhotonPt);
      hsubleadingPhoEta_beforecuts->Fill(subleadingPhotonEta);
      hsubleadingPhoPhi_beforecuts->Fill(subleadingPhotonPhi);

    }

    // bool passedAllCuts = ( numFinalState >= 2 && (leadingPhotonPt > leadingPtCut) && (subleadingPhotonPt > subleadingPtCut) && (fabs(leadingPhotonEta) < 1.4442) && (fabs(subleadingPhotonEta) < 1.4442) );
    bool passedAllCuts = true; // no cuts for now, do offline
    if( passedAllCuts ){

        numEventsPassingCuts++;

        //fill histograms
        hleadingPhoPt->Fill(leadingPhotonPt);
        hleadingPhoEta->Fill(leadingPhotonEta);
        hleadingPhoPhi->Fill(leadingPhotonPhi);

        hsubleadingPhoPt->Fill(subleadingPhotonPt);
        hsubleadingPhoEta->Fill(subleadingPhotonEta);
        hsubleadingPhoPhi->Fill(subleadingPhotonPhi);
        subleadingPt_leadingPt->Fill(leadingPhotonPt,subleadingPhotonPt);

        //fill a mass plot
        TLorentzVector leadingPhoton,subleadingPhoton;
        leadingPhoton.SetPtEtaPhiE(leadingPhotonPt,leadingPhotonEta,leadingPhotonPhi,leadingPhotonE);
        subleadingPhoton.SetPtEtaPhiE(subleadingPhotonPt,subleadingPhotonEta,subleadingPhotonPhi,subleadingPhotonE);

        double dPhi = leadingPhoton.DeltaPhi(subleadingPhoton);
        hggDPhi->Fill(dPhi);

        TLorentzVector total = leadingPhoton + subleadingPhoton; // I think this works
        double ggmass = total.M();
        hggMass->Fill( ggmass );
        hggMass_varBinning->Fill( ggmass );

        leadingPt_mgg->Fill(ggmass,leadingPhotonPt);
        subleadingPt_mgg->Fill(ggmass,subleadingPhotonPt);
        dRgg_mgg->Fill( ggmass,leadingPhoton.DeltaR(subleadingPhoton) );
        dEtagg_mgg->Fill( ggmass,leadingPhoton.Eta() - subleadingPhoton.Eta() );
        dPhigg_mgg->Fill(ggmass,dPhi);

        // fill the tree if option is requested
        if( makeTree ){

          PhotonPt.push_back(leadingPhotonPt);
          PhotonPt.push_back(subleadingPhotonPt);
          PhotonEta.push_back(leadingPhotonEta);
          PhotonEta.push_back(subleadingPhotonEta);
          PhotonPhi.push_back(leadingPhotonPhi);
          PhotonPhi.push_back(subleadingPhotonPhi);
          PhotonEnergy.push_back(leadingPhotonE);
          PhotonEnergy.push_back(subleadingPhotonE);
          massHolder = ggmass;

          tree->Fill();

          PhotonPt.clear();
          PhotonEta.clear();
          PhotonPhi.clear();
          PhotonEnergy.clear();
          pdgId.clear();
          // mother1.clear();
          // mother2.clear();
          GenPt.clear();
          GenEta.clear();
          GenPhi.clear();
          GenEnergy.clear();
          massHolder = -1.;
     
        }


        // if (ggmass > maxMass) maxMass = ggmass;

        // if (ggmass < 200.){
        //   cout << "---------- ggMass < 0.1 GeV! ----------" << endl;
        //   cout << "" << endl;
        //   cout << "ggMass: " << ggmass << endl;
        //   cout << "leadingPhotonPt: " << leadingPhotonPt << endl;
        //   cout << "leadingPhotonEta: " << leadingPhotonEta << endl;
        //   cout << "leadingPhotonPhi: " << leadingPhotonPhi << endl;
        //   cout << "leadingPhotonEnergy: " << leadingPhotonE << endl;
        //   cout << "" << endl;
        //   cout << "subleadingPhotonPt: " << subleadingPhotonPt << endl;
        //   cout << "subleadingPhotonEta: " << subleadingPhotonEta << endl;
        //   cout << "subleadingPhotonPhi: " << subleadingPhotonPhi << endl;
        //   cout << "subleadingPhotonEnergy: " << subleadingPhotonE << endl;
        //   cout << "" << endl;
        //   cout << "-------------------------------------" << endl;

        // } //end if ggMass < 200 block
    } //end if numPhotons >=2 block

}


// ------------ method called once each job just before starting event loop  ------------
void 
DiphotonAnalyzer::beginJob()
{
    hNumPhotons = fs->make<TH1D>("hNumPhotons","Photon Multiplicity (|#eta|<1.4442)",11,-0.5,10.5);
    hggMass = fs->make<TH1D>("hggMass","",172,0,8600.);

    // variable binning

    // 0-640.0 GeV
    // 640-1130.0 GeV
    // 1130-1810.0 GeV
    // 1810-2610.0 GeV
    // 2610-3510.0 GeV
    // >3510 GeV 
    Double_t bins[7] = {0.,650.,1150.,1800.,2600.,3500.,13000.};
    hggMass_varBinning = fs->make<TH1D>("hggMass_varBinning","",6,bins);

    hggDPhi = fs->make<TH1D>("hggDPhi","",300,-3.141593,3.141593);
    hleadingPhoPt = fs->make<TH1D>("hleadingPhoPt","Leading Photon pT",1800.,0,1800.);
    hleadingPhoEta = fs->make<TH1D>("hleadingPhoEta","Leading Photon #eta",100,-1.5,1.5);
    hleadingPhoPhi = fs->make<TH1D>("hleadingPhoPhi","Leading Photon #varphi",100,-3.1416,3.1416);
    hsubleadingPhoPt = fs->make<TH1D>("hsubleadingPhoPt","Subleading Photon pT",1800.,0,1800.);
    hsubleadingPhoEta = fs->make<TH1D>("hsubleadingPhoEta","Subleading Photon #eta",100,-1.5,1.5);
    hsubleadingPhoPhi = fs->make<TH1D>("hsubleadingPhoPhi","Subleading Photon #varphi",100,-3.1416,3.1416);

    hleadingPhoPt_beforecuts = fs->make<TH1D>("hleadingPhoPt_beforecuts","Leading Photon pT",1800.,0,1800.);
    hleadingPhoEta_beforecuts = fs->make<TH1D>("hleadingPhoEta_beforecuts","Leading Photon #eta",400,-6.,6.);
    hleadingPhoPhi_beforecuts = fs->make<TH1D>("hleadingPhoPhi_beforecuts","Leading Photon #varphi",100,-3.1416,3.1416);
    hsubleadingPhoPt_beforecuts = fs->make<TH1D>("hsubleadingPhoPt_beforecuts","Subleading Photon pT",1800.,0,1800.);
    hsubleadingPhoEta_beforecuts = fs->make<TH1D>("hsubleadingPhoEta_beforecuts","Subleading Photon #eta",400,-6.,6.);
    hsubleadingPhoPhi_beforecuts = fs->make<TH1D>("hsubleadingPhoPhi_beforecuts","Subleading Photon #varphi",100,-3.1416,3.1416);

    allPhotonPt = fs->make<TH1D>("allPhotonPt","",1800,0,1800.);
    allPhotonEta = fs->make<TH1D>("allPhotonEta","",100,-6.,6.);
    allPhotonPhi = fs->make<TH1D>("allPhotonPhi","",100,-3.1416,3.1416);

    subleadingPt_leadingPt = fs->make<TH2D>("subleadingPt_leadingPt","",1800,0,1800.,1800,0,1800.);
    leadingPt_mgg = fs->make<TH2D>("leadingPt_mgg","",172,0,8600.,1800,0,1800.);
    subleadingPt_mgg = fs->make<TH2D>("subleadingPt_mgg","",172,0,8600.,1800,0,1800.);
    dRgg_mgg = fs->make<TH2D>("dRgg_mgg","",172,0,8600.,100,0,10.);
    dEtagg_mgg = fs->make<TH2D>("dEtagg_mgg","",172,0,8600.,100,-1.5,1.5);
    dPhigg_mgg = fs->make<TH2D>("dPhigg_mgg","",172,0,8600.,100,-3.1416,3.1416);

    //tree stuff
    if( makeTree ){
      tree = fs->make<TTree>("tree","tree");
      tree->Branch("PhotonPt",&PhotonPt);
      tree->Branch("PhotonEta",&PhotonEta);
      tree->Branch("PhotonPhi",&PhotonPhi);
      tree->Branch("PhotonEnergy",&PhotonEnergy);
      tree->Branch("pdgId",&pdgId);
      // tree->Branch("mother1",&mother1);
      // tree->Branch("mother2",&mother2);
      tree->Branch("GenPt",&GenPt);
      tree->Branch("GenEta",&GenEta);
      tree->Branch("GenPhi",&GenPhi);
      tree->Branch("GenEnergy",&GenEnergy);
      tree->Branch("ggMass",&massHolder,"ggMass/D");
    }
    
}

// ------------ method called once each job just after ending the event loop  ------------
void 
DiphotonAnalyzer::endJob() 
{
    hggMass->GetXaxis()->SetTitle("M_{#gamma#gamma} (GeV/c^{2})");
    if( leptonMode ){
      std::cout << "Electron Count: " << numElectrons << std::endl;
      std::cout << "Muon Count: " << numMuons << std::endl;
    }
    std::cout << "Number of Events Passing Cuts: " << numEventsPassingCuts << std::endl;
    std::cout << "Number of Total Events: " << numTotalEvents << std::endl;
    std::cout << "--> Cut Efficiency = " << (1.0*numEventsPassingCuts)/(1.0*numTotalEvents) << std::endl;
    // std::cout << "Largest diphoton invariant mass: " << maxMass << std::endl;
}

// ------------ method called when starting to processes a run  ------------
void 
DiphotonAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a run  ------------
void 
DiphotonAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}

// ------------ method called when starting to processes a luminosity block  ------------
void 
DiphotonAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method called when ending the processing of a luminosity block  ------------
void 
DiphotonAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DiphotonAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DiphotonAnalyzer);

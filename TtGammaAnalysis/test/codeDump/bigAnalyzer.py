
# analyzer for genParticle related stuff (all photons)
patPhotonAnalyzerAll = cms.EDAnalyzer(
    "PATPhotonHistoAnalyzer",
    src = cms.InputTag("photonsWithGenPart"),
    histograms = cms.VPSet(
            cms.PSet(min          = cms.untracked.double(     -250.5),
                     max          = cms.untracked.double(      250.5),
                     nbins        = cms.untracked.int32 (        501),
                     name         = cms.untracked.string( 'motherId'),
                     description  = cms.untracked.string('mother: pdgId;pdgId;count'),
                     plotquantity = cms.untracked.string('genParticle.mother.pdgId')
                     ),        
            cms.PSet(min          = cms.untracked.double(        0.),
                     max          = cms.untracked.double(       500),
                     nbins        = cms.untracked.int32 (       100),
                     name         = cms.untracked.string('pt'),
                     description  = cms.untracked.string('p_{T};p_{T} / GeV;count'),
                     plotquantity = cms.untracked.string('pt')
                     ),
            cms.PSet(min          = cms.untracked.double(      -0.5),
                     max          = cms.untracked.double(      10.5),
                     nbins        = cms.untracked.int32 (        11),
                     name         = cms.untracked.string('NumOverlaps'),
                     description  = cms.untracked.string('Number of overlap jets in #DeltaR = 0.5;no.;count'),
                     plotquantity = cms.untracked.string('overlaps("jets").size')
                     ),
            cms.PSet(min          = cms.untracked.double(      -1.5),
                     max          = cms.untracked.double(      30.5),
                     nbins        = cms.untracked.int32 (        32),
                     name         = cms.untracked.string('overlapsJetsNumConstituents'),
                     description  = cms.untracked.string('Number of overlap jet constituents;no.;count'),
                     lazyParsing  = cms.untracked.bool(True),
                     plotquantity = cms.untracked.string('\
? overlaps("jets").size > 0 ? overlaps("jets")[0].getPFConstituents.size : -1 \
                                                           ')
                     ),
            cms.PSet(min          = cms.untracked.double(        0.),
                     max          = cms.untracked.double(       0.7),
                     nbins        = cms.untracked.int32 (        14),
                     name         = cms.untracked.string('dR(photon, Jet)'),
                     description  = cms.untracked.string('dR(photon, Jet);dR(photon, Jet);count'),
                     plotquantity = cms.untracked.string('\
? overlaps("jets").size > 0 ?\
 deltaR(eta, phi, overlaps("jets")[0].eta, overlaps("jets")[0].phi) : -1 \
                                                           ')
                     ),
            cms.PSet(min          = cms.untracked.double(     -50.5),
                     max          = cms.untracked.double(      50.5),
                     nbins        = cms.untracked.int32 (       101),
                     name         = cms.untracked.string('pdgIdFor1ParticleJets'),
                     description  = cms.untracked.string('pdgId of 1 part. jet constituent;pdgId;count'),
                     lazyParsing  = cms.untracked.bool(True),
                     plotquantity = cms.untracked.string('\
? overlaps("jets").size == 1 && overlaps("jets")[0].getPFConstituents.size == 1 ?\
 overlaps("jets")[0].getPFConstituents[0].pdgId  : -300 \
                                                           ')
                     )
        )
)

# analyzer for genParticle related stuff (all photons)
patPhotonsFromMEAnalyzer = patPhotonAnalyzerAll.clone(
        src = cms.InputTag("patPhotonsFromME")
)
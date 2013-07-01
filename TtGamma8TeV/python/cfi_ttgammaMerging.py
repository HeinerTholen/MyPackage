
import FWCore.ParameterSet.Config as cms
from SimGeneral.HepPDTESSource.pythiapdt_cfi import *
from TopQuarkAnalysis.TopEventProducers.sequences.ttGenEvent_cff import *

#ttbarPhotonMergerLegacy = cms.EDFilter("TTGammaMergerLegacy",
#    ptCut = cms.double(20.),
#    drCut = cms.double(.1),
##    is2to7 = cms.untracked.bool(True),
#    is2to5 = cms.untracked.bool(True),
#    filter = cms.bool(True),
#)

ttbarPhotonMerger = cms.EDFilter("TTGammaMerger",
    ptCut = cms.double(20.),
    drCut = cms.double(.1),
    filter = cms.bool(True),
)

ttbarPhotonMergerSingleCall = ttbarPhotonMerger.clone()

ttgammaMerging = cms.Sequence(
#    makeGenEvt *
    ttbarPhotonMerger
)



cmsDriver.py \
MyPackage/TtGammaAnalysis/python/myGenFragment.py \
-s GEN,FASTSIM,HLT:GRun \
--conditions=FrontierConditions_GlobalTag,START42_V13::All \
--eventcontent=RECOSIM \
--filetype=LHE \
--filein=file:/home/home2/institut_3b/tholen/dev/ttgamma/forProduction20120330/ttbar_43.lhef \
--fileout=file:/user/tholen/eventFiles/ttgamma_whizard_43.root \
-n 10000 \
--no_exec 


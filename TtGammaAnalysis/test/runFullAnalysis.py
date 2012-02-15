
import os
from YKuessel.TopCharge.sourceFiles_cfi import *

input = "/user/tholen/eventFiles/Samplelist_Background.txt"
dictOfLists = ReadProdDetails(input)

for i, sample in enumerate(dictOfLists["abbreviation"]):
    cmsRun='cmsRun test/runAnalysisOnSample_cfg.py ' + str(sample) + ' &> outputLogs/runFullAnalysis_' + str(sample) + '.log'
    #if (i % 3 != 2):
    #    cmsRun = cmsRun + " &"
    print cmsRun
    os.system(cmsRun)

        

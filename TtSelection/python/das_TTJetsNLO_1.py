import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1000_1_wQd.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1003_1_8UM.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1004_1_dcA.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1005_1_bqn.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1007_1_r5v.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1008_1_4iX.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1009_1_PkG.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_100_1_Slk.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1010_1_fLd.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1011_1_7jp.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1012_1_G2r.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1013_1_uo4.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1014_1_YD7.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1015_1_B6e.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1016_1_CQy.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1017_1_2Ey.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1018_1_SSj.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1019_1_5zL.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_101_1_Xmy.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1020_1_IYc.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1021_1_4mI.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1022_1_wYE.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1023_1_MD0.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1024_1_5DA.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1025_1_9Eg.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1028_1_X8B.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1029_1_40X.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_102_1_Q14.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1030_1_7fW.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1031_1_5ns.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1032_1_Lax.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1033_1_0RS.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1034_1_AwD.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1035_1_SBd.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1036_1_Qww.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1037_1_2Ps.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1038_1_Nct.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1039_1_qKV.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_103_1_FX4.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1040_1_ZQv.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1041_1_jzW.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1042_1_p4L.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1043_1_JTR.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1044_1_Qbs.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1045_1_CjJ.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1046_1_v12.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1047_1_3Pc.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1048_1_H7h.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1049_1_R1J.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_104_1_OO4.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1050_1_sZh.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1051_1_UEE.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1052_1_Auk.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1054_1_pkt.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1055_1_bus.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1057_1_ZYN.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1058_1_nvb.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_105_1_dYH.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1060_1_Kue.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1061_1_SvC.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1062_1_LtP.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1063_1_1CP.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1064_1_amP.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1065_1_J5z.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1067_1_42w.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1068_1_SDy.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1069_1_BnG.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_106_1_yk1.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1070_1_wiG.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1071_1_6QO.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1072_1_pFJ.root',
       '/store/user/htholen/TT_8TeV-mcatnlo/TTJets_MCatNLO_patTuple/59f484fc9b4a422135c150500bf194d2/patTuple_1074_1_SQv.root',
             ] );


secFiles.extend( [
               ] )


import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_103_1_sQN.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_104_1_YxL.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_105_1_pIu.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_107_1_nMI.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_108_1_aS3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_100_1_O7f.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_10_1_iWD.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_110_1_bjF.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_101_1_jlo.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_102_1_x94.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_113_1_alA.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_114_1_bvy.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_106_1_1TE.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_109_1_shR.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_111_1_McP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_118_1_5hP.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_112_1_KcX.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_115_1_x9w.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_120_1_jsd.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_116_1_BDo.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_117_1_7lb.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_123_1_Bo8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_124_1_feI.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_119_2_jGD.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_11_1_AZt.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_127_1_rUZ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_128_1_o2J.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_121_1_Wg3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_12_1_GTT.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_130_1_vgn.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_131_1_ZGs.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_132_1_pie.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_133_1_gqt.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_122_1_yMM.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_125_1_udK.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_136_1_OBO.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_137_1_tBv.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_126_1_ry4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_129_1_Kc5.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_13_1_hrs.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_134_1_4cQ.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_135_1_sqE.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_138_1_ONw.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_139_1_sZD.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_144_1_9iY.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_140_1_gsr.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_141_1_Njr.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_147_1_rg8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_142_2_60a.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_149_2_AXI.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_14_1_1Lm.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_150_1_zHF.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_143_1_fLy.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_152_1_YsV.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_153_1_FVR.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_154_1_9Xx.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_155_1_786.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_145_1_2rz.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_157_1_d5B.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_158_1_6ff.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_146_1_y1R.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_148_1_WEN.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_160_1_Q6G.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_151_1_8wR.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_156_1_245.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_159_1_7Ib.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_164_1_wXO.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_165_1_yjy.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_166_1_2vH.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_15_1_QxK.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_168_1_rDA.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_169_1_zhK.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_16_1_as3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_170_1_gp9.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_161_1_smB.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_162_1_lj5.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_173_1_veB.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_163_1_iD9.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_175_1_gXG.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_176_2_me4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_167_1_Shk.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_171_1_MAf.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_172_1_SJB.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_174_1_rq6.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_177_1_Wdg.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_178_1_1rx.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_179_1_xfw.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_183_2_ru8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_184_1_x8w.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_17_1_PmE.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_180_1_uGw.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_187_1_f1A.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_188_1_BN9.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_181_1_C6A.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_9_1_JOW.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_18_1_emL.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_99_1_I9v.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_190_1_6W4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_98_1_V9a.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_191_1_GMb.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_97_1_wo2.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_192_2_sR4.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_96_1_3In.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_193_1_hW7.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_95_1_xCS.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_182_1_0Fi.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_94_1_cB7.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_185_2_hVa.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_93_1_6bC.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_196_1_hOr.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_197_1_4N3.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_186_1_q8B.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_199_1_4Wb.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_19_1_o7X.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_189_1_gv5.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_200_1_7H8.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_201_1_qGc.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_194_1_DTv.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_203_1_kkS.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_195_1_y5i.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_205_1_jDW.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_206_1_65x.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_207_1_Tb9.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_208_1_3hU.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_198_3_ac9.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_20_1_ex2.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_210_1_keM.root',
       '/store/user/htholen/LHE2EDM_WHIZARD_2to5_ttA/AODSIM_WHIZARD_2to5_ttA/fe74fcc77c246270c50934efd2ef6884/out_GENSTEP_1_1_aEg.root' ] );

secFiles.extend( [
               ] )

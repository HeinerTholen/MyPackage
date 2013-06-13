import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring() 
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_100_1_tSm.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_101_1_WE8.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_102_1_YTR.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_103_1_qEy.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_104_1_Bdf.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_105_1_x6w.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_108_1_0hy.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_106_1_rSw.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_107_1_Kx9.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_109_1_NEw.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_10_2_XzB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_110_1_GkF.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_111_1_wyk.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_112_1_mdE.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_113_1_6lV.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_114_1_YN2.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_115_1_uAv.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_116_1_5a8.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_117_1_qon.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_118_1_72U.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_119_1_b7h.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_11_2_kSU.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_120_1_ZVA.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_121_1_UiP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_122_1_uom.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_123_1_cGo.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_124_1_BrB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_125_1_c6K.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_126_1_2ZS.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_127_1_UIy.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_128_1_lbZ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_129_1_Z7Y.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_12_2_qaU.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_130_1_0EP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_131_1_27Y.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_132_1_90p.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_133_1_2PP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_134_1_FZn.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_135_1_idk.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_136_1_NQh.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_137_1_hUt.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_138_1_sgh.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_139_1_YIS.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_13_2_sbT.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_140_1_ZeI.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_141_1_c7h.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_142_1_XbD.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_145_1_sqQ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_143_1_kge.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_144_1_BO4.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_146_1_U4J.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_147_1_9ki.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_148_1_Mhg.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_149_1_nSG.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_14_2_8i6.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_150_1_CSB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_151_1_U2F.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_152_1_gUR.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_153_1_fWh.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_154_1_r8T.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_155_1_Lgn.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_156_1_ZqT.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_157_1_sbT.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_158_1_PCq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_159_1_B1A.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_15_2_Bbf.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_160_1_mic.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_161_1_H9g.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_162_1_UE2.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_163_1_hxq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_164_1_rBX.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_165_1_obk.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_166_1_Syf.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_167_1_8DJ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_168_1_Di0.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_169_1_FvU.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_171_1_W0p.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_16_2_oB5.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_170_1_PfZ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_172_1_KVM.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_173_2_IoF.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_174_1_VAs.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_175_2_cYx.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_176_2_lei.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_177_2_iVh.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_17_2_YUa.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_178_2_6nD.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_179_2_tPU.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_180_1_nmG.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_181_2_2cJ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_182_1_kv8.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_183_1_2Fu.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_184_2_DEk.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_185_1_kGK.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_186_1_lbv.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_187_1_pyr.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_188_1_9L0.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_189_2_0uq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_191_1_U0r.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_18_2_Dow.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_190_1_xZP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_192_1_Iab.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_193_1_qam.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_194_1_dPs.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_195_2_bRY.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_196_2_UZn.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_197_2_bD8.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_198_1_ztG.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_199_2_g4n.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_19_2_hMQ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_1_2_Soi.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_200_1_YUK.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_201_2_V8C.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_202_1_HEI.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_203_2_xNh.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_204_1_LyO.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_205_1_ZQO.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_206_1_y4i.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_207_1_T91.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_208_1_MBC.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_209_1_ILg.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_20_2_XOP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_210_1_V6l.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_211_1_BBn.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_214_1_97r.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_212_1_HC1.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_213_1_XE0.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_215_1_6vo.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_216_1_7KN.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_217_1_n2A.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_218_1_Wm7.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_219_1_aJq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_21_2_uNV.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_220_1_elQ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_221_1_ger.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_222_1_Jpc.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_223_1_7hG.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_224_1_axB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_225_1_cI4.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_226_1_jRC.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_227_1_xrC.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_228_1_olk.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_229_1_Duf.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_22_2_O9z.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_230_1_ISe.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_231_1_sd0.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_232_1_Sa5.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_236_1_obn.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_233_1_Qbz.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_234_1_oTB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_235_1_5mQ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_237_1_YeA.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_238_1_0xX.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_239_1_TKj.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_23_2_Wkg.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_240_1_5iQ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_241_1_n9n.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_242_1_R6f.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_243_1_Obj.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_244_1_MMA.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_245_1_nxG.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_246_1_qnT.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_247_1_fKH.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_248_1_rDH.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_251_1_lWq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_249_1_aEB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_24_2_spy.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_250_1_8MP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_252_1_HXn.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_253_1_vmP.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_254_1_P0g.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_255_1_M71.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_256_1_Vrq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_257_1_uWs.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_258_1_qgi.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_259_1_goQ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_25_2_tMB.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_260_1_jof.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_261_1_o2D.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_262_1_Wl7.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_263_1_Zt7.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_264_1_FO9.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_265_1_OD6.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_266_1_M5F.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_267_2_eGd.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_268_1_rcz.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_269_1_cpf.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_26_2_Hbg.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_270_1_Pgp.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_271_1_lcE.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_272_1_l9a.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_273_1_SDp.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_274_1_hQW.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_275_1_zLR.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_276_1_x48.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_277_1_0v2.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_278_1_zE6.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_279_1_flW.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_27_2_4Cq.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_280_1_zTW.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_281_1_RQZ.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_282_1_ec9.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_283_1_Zw6.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_284_1_iVi.root',
       '/store/user/kuessel/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/YK_MC_MARCH13_WJets/accebdcbeca2810af478d8af2493d41f/SynchSelMuJets_285_1_Mfc.root' ] );


secFiles.extend( [
               ] )

# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: sherpa_ZJets_MASTER_cff.py -s GEN -n 100 --no_exec --conditions auto:mc --eventcontent RAWSIM
import FWCore.ParameterSet.Config as cms



process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic50ns13TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('sherpa_ZJets_MASTER_cff.py nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(1),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('sherpa_ZJets_MASTER_cff_py_GEN.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

process.generator = cms.EDFilter("SherpaGeneratorFilter",
  maxEventsToPrint = cms.int32(0),
  filterEfficiency = cms.untracked.double(1.0),
  crossSection = cms.untracked.double(-1),
  SherpaProcess = cms.string('DYLOM'),
  SherpackLocation = cms.string('/afs/desy.de/user/h/hinzmann/public/'),
  SherpackChecksum = cms.string('28fffe66e4a2ad277410f17888cadaa9'),
  FetchSherpack = cms.bool(True),
  SherpaPath = cms.string('./'),
  SherpaPathPiece = cms.string('./'),
  SherpaResultDir = cms.string('Result'),
  SherpaDefaultWeight = cms.double(1.0),
  SherpaParameters = cms.PSet(parameterSets = cms.vstring(
                             "MPI_Cross_Sections",
                             "Run"),
                              MPI_Cross_Sections = cms.vstring(
				" MPIs in Sherpa, Model = Amisic:",
				" semihard xsec = 39.6936 mb,",
				" non-diffractive xsec = 17.0318 mb with nd factor = 0.3142."
                                                  ),
                              Run = cms.vstring(
				" (run){",
				" EVENTS 10000; ERROR 0.99;",
				" FSF:=1.; RSF:=1.; QSF:=1.;",
				" Rjet:=0.4;",
				" RJsq:=Rjet*Rjet;",
				" SCALES METS{FSF*MU_F2}{RSF*MU_R2}{RJsq*QSF*MU_Q2};",
				" NJET:=1; LJET:=2,3,4; QCUT:=30.;",
				" ME_SIGNAL_GENERATOR Comix Amegic;",
				" EVENT_GENERATION_MODE W;",
				" BEAM_1 2212; BEAM_ENERGY_1 = 6500.;",
				" BEAM_2 2212; BEAM_ENERGY_2 = 6500.;",
				" MAX_PROPER_LIFETIME = 10.0",
				"}(run)",
				" (processes){",
				" Process 93 93 -> 13 -13 93 93{NJET};",
				" Order (*,2); CKKW sqr(QCUT/E_CMS);",
				" Cut_Core 1;",
				" Integration_Error 0.02 {3};",
				" Integration_Error 0.02 {4};",
				" Integration_Error 0.02 {5};",
				" End process;",
				"}(processes)",
				" (selector){",
				" Mass 13 -13 70 110",
				" FastjetFinder antikt 1 25 0.0 Rjet;",
				"}(selector)",
				" (analysis){",
				" BEGIN_RIVET {",
				" -a PAPER_FIN_R8",
				"} END_RIVET;",
				"}(analysis)"
                                                  ),
                             )
)


process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.endjob_step,process.RAWSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path).insert(0, process.ProductionFilterSequence)

# customisation of the process.
process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')

# Automatic addition of the customisation function from Configuration.GenProduction.rivet_customize
#from Configuration.GenProduction.rivet_customize import customise 

def customise(process):
	process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
        process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_2018_PAS_SMP_18_QGX_ZPJ')
## DIJET
## CMS_2018_PAS_SMP_18_QGX_DIJET
## ZPJ
## CMS_2018_PAS_SMP_18_QGX_ZPJ
## UE
## CMS_Internal_FSQ_15_007','CMS_FSQ_15_008','CMS_2015_I1384119','ATLAS_2016_I1419652','CMS_FSQ_15_005','CMS_FSQ_15_006

	process.rivetAnalyzer.CrossSection = cms.double(4.956e+09)

##  DIJET
##  TimeShower:alphaSvalue
##  0.118      0.113      0.123
##  4.956e+09  4.948e+09  4.937e+09
##
##  ZPJ
##  TimeShower:alphaSvalue
##  0.118      0.113      0.123
##  1.339e+03  1.333e+03  1.338e+03
##
##  Underlying Events
##  TimeShower:alphaSvalue
##  0.118      0.113      0.123      0.100      0.136
##  7.842e+10  7.842e+10  7.842e+10  7.842e+10  7.842e+10

##  ALL 4 ALPHA_S-VALUES CHANGED
##  DIJET
##  TimeShower:alphaSvalue
##  0.118      0.113      0.123      0.100      0.136
##  4.956e+09  4.374e+09  5.622e+09  3.147e+09  7.576e+09
##
##  ZPJ
##  TimeShower:alphaSvalue
##  0.118      0.113      0.123      0.100      0.136
##  1.339e+03  1.201e+03  1.401e+03  1.100e+03  1.584e+03
##
##  Underlying Events
##  TimeShower:alphaSvalue
##  0.118      0.113      0.123      0.100      0.136
##  7.842e+10  7.842e+10  7.842e+10  7.842e+10  7.842e+10

        process.rivetAnalyzer.OutputFile = cms.string('DY_Sherpa_LOM_Mar16.yoda')
	process.rivetAnalyzer.UseExternalWeight = cms.bool(True)
	process.rivetAnalyzer.useGENweights = cms.bool(True)
	process.generation_step+=process.rivetAnalyzer
	process.schedule.remove(process.RAWSIMoutput_step)
        return(process)      
#call to customisation function customise imported from Configuration.GenProduction.rivet_customize
process = customise(process)

# End of customisation functions

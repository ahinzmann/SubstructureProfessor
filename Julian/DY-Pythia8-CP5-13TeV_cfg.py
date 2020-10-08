import FWCore.ParameterSet.Config as cms
import os

process = cms.Process('GEN')

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic7TeV2011Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.3 $'),
    annotation = cms.untracked.string('PYTHIA6-MinBias TuneZ2 at 7TeV'),
    name = cms.untracked.string('$Source: /local/reps/CMSSW/CMSSW/Configuration/GenProduction/python/Attic/MinBias_TuneZ2_7TeV_pythia6_cff.py,v $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    splitLevel = cms.untracked.int32(0),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    fileName = cms.untracked.string('MinBias_TuneZ2_7TeV_pythia6_cff_py_GEN.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string(''),
        dataTier = cms.untracked.string('GEN-SIM-RAW')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    )
)

# Additional output definition
process.MessageLogger.cerr.FwkReport.reportEvery = 10000

# Other statements
process.GlobalTag.globaltag = 'MCRUN2_74_V9A'

pythia8CommonSettingsBlock = cms.PSet(
    pythia8CommonSettings = cms.vstring(
      'Tune:preferLHAPDF = 2',
      'Main:timesAllowErrors = 10000',
      'Check:epTolErr = 0.01',
      'Beams:setProductionScalesFromLHEF = off',
      'SLHA:keepSM = on',
      'SLHA:minMassSM = 1000.',
      'ParticleDecays:limitTau0 = on',
      'ParticleDecays:tau0Max = 10',
      'ParticleDecays:allowPhotonRadiation = on',
    )
)

pythia8CP5SettingsBlock = cms.PSet(
    pythia8CP5Settings = cms.vstring(
        'Tune:pp 14',
        'Tune:ee 7',
        'MultipartonInteractions:ecmPow=0.03344',
        'MultipartonInteractions:bProfile=2',
        'MultipartonInteractions:pT0Ref=1.41',
        'MultipartonInteractions:coreRadius=0.7634',
        'MultipartonInteractions:coreFraction=0.63',
        'ColourReconnection:mode=0', # 0
        'ColourReconnection:range=5.176',
        'SigmaTotal:zeroAXB=off',
        'SpaceShower:alphaSorder=2',
        'SpaceShower:alphaSvalue=0.118', # 0.118
        'SigmaProcess:alphaSvalue=0.118',
        'SigmaProcess:alphaSorder=2',
        'MultipartonInteractions:alphaSvalue=0.118',
        'MultipartonInteractions:alphaSorder=2',
        'TimeShower:alphaSorder=2',
        'TimeShower:alphaSvalue=0.118', # 0.118
##  0.118  0.113  0.123
        'TimeShower:pTmin=0.5', # 0.5 from Monash 2013
##  0.5  0.45  0.55  0.2  0.8
        'SigmaTotal:mode = 0',
        'SigmaTotal:sigmaEl = 21.89',
        'SigmaTotal:sigmaTot = 100.309',
        'PDF:pSet=LHAPDF6:NNPDF31_nnlo_as_0118',
        #'TimeShower:scaleGluonToQuark=<__TimeShower:scaleGluonToQuark__>', # 1 Pythia default
        )
)

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(1.0),
        filterEfficiency = cms.untracked.double(1.0),
        maxEventsToPrint = cms.untracked.int32(1),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(1),

        PythiaParameters = cms.PSet(
                pythia8CommonSettingsBlock, 
                pythia8CP5SettingsBlock, 
                processParameters = cms.vstring(
                        ## switch on for DIJET
                        # 'HardQCD:all = on',
                        ## switch on for ZPJ
                         'WeakBosonAndParton:qqbar2gmZg = on', 
                         'WeakBosonAndParton:qg2gmZq = on',    
                         'WeakBosonAndParton:fgm2gmZf = on',
                         '23:onMode = off',
                         '23:onIfAny = 13',
                        ## switch on for UE
                        #'SoftQCD:nonDiffractive = on',
                        #'SoftQCD:singleDiffractive = on',
                        #'SoftQCD:centralDiffractive = on',
                        #'SoftQCD:doubleDiffractive = on',
                        ## switch on for DIJET and ZPJ
                         'PhaseSpace:pTHatMin = 15',
                         'PhaseSpace:pTHatMax = 7000',
                         'PhaseSpace:bias2Selection = on',
                         'PhaseSpace:bias2SelectionPow = 4.5',
                         'PhaseSpace:bias2SelectionRef = 15.',
                ),
                parameterSets = cms.vstring('pythia8CommonSettings',
                                            'pythia8CP5Settings', 
                                            'processParameters', 
                                            )
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
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

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

	process.rivetAnalyzer.CrossSection = cms.double(1.339e+03)

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

        process.rivetAnalyzer.OutputFile = cms.string('DY_Pythia8_CP5_Oct7.yoda')
	process.rivetAnalyzer.UseExternalWeight = cms.bool(True)
	process.rivetAnalyzer.useGENweights = cms.bool(True)
	process.generation_step+=process.rivetAnalyzer
	process.schedule.remove(process.RAWSIMoutput_step)
        return(process)      
#call to customisation function customise imported from Configuration.GenProduction.rivet_customize
process = customise(process)

# End of customisation functions

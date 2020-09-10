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

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
                                 comEnergy = cms.double(13000.0),
                                 crossSection = cms.untracked.double(9.573213e+08),
                                 filterEfficiency = cms.untracked.double(1),
                                 maxEventsToPrint = cms.untracked.int32(0),
                                 pythiaHepMCVerbosity = cms.untracked.bool(False),
                                 pythiaPylistVerbosity = cms.untracked.int32(0),
                                 PythiaParameters = cms.PSet(
        processParameters = cms.vstring(
        'Main:timesAllowErrors    = 10000',
        'ParticleDecays:limitTau0 = on',
        'ParticleDecays:tauMax = 10',
        'SoftQCD:nonDiffractive = on',
        'SoftQCD:singleDiffractive = on',
        'SoftQCD:doubleDiffractive = on',
        'SoftQCD:centralDiffractive = on',
        'PhaseSpace:pTHatMin = 0', 
        'PhaseSpace:pTHatMax = 7000',
        'PhaseSpace:mHatMin = 0',  
        'PhaseSpace:mHatMax = 7000',
        'Tune:pp 14',
        'Tune:ee 7',
        'PDF:pSet=17',
        'SpaceShower:rapidityOrder=off',
        'SigmaTotal:zeroAXB=off',
        'StringZ:aLund = 0.38',
        'StringZ:bLund = 0.64',
        'StringFlav:probQQtoQ = 0.078',
        'StringFlav:probStoUD = 0.2',
        'MultipartonInteractions:bProfile=2',
        'MultipartonInteractions:ecmPow=0.1129',
        'MultipartonInteractions:pT0Ref=1.984',
        'MultipartonInteractions:coreRadius=0.746',
        'MultipartonInteractions:coreFraction=0.5687',
        'ColourReconnection:mode = 1',
        'BeamRemnants:remnantMode=1',
        'ColourReconnection:timeDilationPar=31.07',
        'ColourReconnection:m0=1.845',
        'ColourReconnection:junctionCorrection=8.382',
        ),
        parameterSets = cms.vstring('processParameters')
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
        process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_Internal_FSQ_15_007','CMS_FSQ_15_008','CMS_2015_I1384119','ATLAS_2016_I1419652','CMS_FSQ_15_005','CMS_FSQ_15_006')
	process.rivetAnalyzer.CrossSection = cms.double(7.106e+10)

##  TimeShower:alphaSvalue
##  0.118     0.113     0.123     0.098     0.138
##  4.914e+09 4.895e+09 4.909e+09 4.910e+09 4.909e+09
##  TimeShower:pTmin
##  0.5       0.45      0.55      0.2       0.8
##  4.914e+09 4.891e+09 4.914e+09 4.903e+09 4.925e+09
##
##  Underlying Events
##  TimeShower:alphaSvalue
##  0.118     0.123
##  7.805e+10 7.805e+10

        process.rivetAnalyzer.OutputFile = cms.string('TuneCP1_CP1_CR1_UE.yoda')
	process.rivetAnalyzer.UseExternalWeight = cms.bool(True)
	process.rivetAnalyzer.useGENweights = cms.bool(True)
	process.generation_step+=process.rivetAnalyzer
	process.schedule.remove(process.RAWSIMoutput_step)
        return(process)      
#call to customisation function customise imported from Configuration.GenProduction.rivet_customize
process = customise(process)

# End of customisation functions

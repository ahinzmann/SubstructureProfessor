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
    input = cms.untracked.int32(1000000)
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
process.MessageLogger.cerr.FwkReport.reportEvery = 1000000

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
        'MultipartonInteractions:ecmPow=0.05357',
        'PDF:pSet=20',
        'MultipartonInteractions:bProfile=2',
        'MultipartonInteractions:pT0Ref=1.454',
        'MultipartonInteractions:coreRadius=0.6489',
        'MultipartonInteractions:coreFraction=0.4881',
        'ColourReconnection:mode=2',
        'ColourReconnection:m2Lambda=4.917',
        'ColourReconnection:fracGluon=0.9927',
        'SigmaTotal:zeroAXB=off',
        'SpaceShower:alphaSorder=2',
        'SpaceShower:alphaSvalue=0.118', # 0.118
        'SigmaProcess:alphaSvalue=0.118',
        'SigmaProcess:alphaSorder=2',
        'MultipartonInteractions:alphaSvalue=0.118',
        'MultipartonInteractions:alphaSorder=2',
        'TimeShower:alphaSorder=2',
        'TimeShower:alphaSvalue=0.118', # 0.118
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
                        'HardQCD:all = on',
                        'PhaseSpace:pTHatMin = 10',
                        'PhaseSpace:pTHatMax = 4000',
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
        process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_2018_SMP_16_010','CMS_2016_I1459051')
	process.rivetAnalyzer.CrossSection = cms.double(1.0)
        process.rivetAnalyzer.OutputFile = cms.string('QCD-13TeV.yoda')
	process.rivetAnalyzer.UseExternalWeight = cms.bool(True)
	process.rivetAnalyzer.useGENweights = cms.bool(True)
	process.generation_step+=process.rivetAnalyzer
	process.schedule.remove(process.RAWSIMoutput_step)
        return(process)      
#call to customisation function customise imported from Configuration.GenProduction.rivet_customize
process = customise(process)

# End of customisation functions
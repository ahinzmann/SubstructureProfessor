# Auto generated configuration file
# using:
# Revision: 1.19
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v
# with command line options: Configuration/GenProduction/python/ThirteenTeV/QCD_Pt-15To7000_TuneCUETP8M1_Flat_13TeV-pythia8_cff.py -s GEN --datatier=GEN-SIM --conditions auto:mc --eventcontent RAWSIM --no_exec -n 10000 --python_filename=RIVET_QCD_Pt-15To7000_TuneCUETP8M1_Flat_13TeV-pythia8_cff.py --customise=Configuration/GenProduction/rivet_customize.py

# NB: run inside CMSSW_7_1_19 to recover original 2016 sample

import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

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
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

process.MessageLogger.cerr.FwkReport.reportEvery = 1000

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/ThirteenTeV/QCD_Pt-15To7000_TuneCUETP8M1_Flat_13TeV-pythia8_cff.py nevts:10000'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(20971520),
    fileName = cms.untracked.string('QCD_Pt-15To7000_TuneCUETP8M1_Flat_13TeV-pythia8_cff_py_GEN.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')

# from Configuration.Generator.Herwig7Settings.Herwig7CH2TuneSettings_cfi import herwig7CH2SettingsBlock
process.generator = cms.EDFilter("Herwig7GeneratorFilter",
    productionParameters = cms.vstring(
        'read snippets/PPCollider.in',
        ## UE
        # 'read snippets/MB.in',
        # 'read snippets/Diffraction.in',
        ## UE ends
        'mkdir /Herwig/Weights',
        'cd /Herwig/Weights',
        'create ThePEG::ReweightMinPT reweightMinPT ReweightMinPT.so',
        'cd /Herwig/MatrixElements/',
        ## DIJET
        # 'insert SubProcess:MatrixElements[0] MEQCD2to2',
        # 'insert SubProcess:Preweights[0] /Herwig/Weights/reweightMinPT',
        ## DIJET ends
        ## ZPJ
        'insert SubProcess:MatrixElements[0] MEZJet',
        'DISABLEREADONLY',
        'newdef MEZJet:ZDecay ChargedLeptons',
        ## ZPJ ends
        'cd /',
        ## ZPJ
        'set /Herwig/Cuts/LeptonPairMassCut:MinMass 60.*GeV',
        ## ZPJ ends
        'set /Herwig/Cuts/JetKtCut:MinKT 20.*GeV',
        'set /Herwig/Cuts/JetKtCut:MaxKT 7000.*GeV',
        'set /Herwig/Cuts/Cuts:MHatMin  0.0*GeV',
        'set /Herwig/Cuts/Cuts:X1Min    1e-07',
        'set /Herwig/Cuts/Cuts:X2Min    1e-07',
        'set /Herwig/Cuts/MassCut:MinM  0.0*GeV',
        'set /Herwig/Weights/reweightMinPT:Power 4.5',
        'set /Herwig/Weights/reweightMinPT:Scale 15*GeV',
        'set /Herwig/Decays/DecayHandler:MaxLifeTime 10*mm',
        'set /Herwig/Decays/DecayHandler:LifeTimeOption Average'
    ),
    parameterSets = cms.vstring('productionParameters'),
    configFiles = cms.vstring(),
    crossSection = cms.untracked.double(1363000000),
    dataLocation = cms.string('${HERWIGPATH:-6}'),
    eventHandlers = cms.string('/Herwig/EventHandlers'),
    filterEfficiency = cms.untracked.double(1.0),
    generatorModule = cms.string('/Herwig/Generators/EventGenerator'),
    repository = cms.string('${HERWIGPATH}/HerwigDefaults.rpo'),
    run = cms.string('InterfaceMatchboxTest'),
    runModeList = cms.untracked.string("read,run"),
)

# Set random number seed
# process.RandomNumberGeneratorService.generator.initialSeed = cms.untracked.uint32(123456789)

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
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq

# customisation of the process.

# Automatic addition of the customisation function from Configuration.GenProduction.rivet_customize
# from Configuration.GenProduction.rivet_customize import customise

#call to customisation function customise imported from Configuration.GenProduction.rivet_customize
# process = customise(process)

process.load('GeneratorInterface.RivetInterface.rivetAnalyzer_cfi')
process.generation_step += process.rivetAnalyzer
process.schedule.remove(process.RAWSIMoutput_step)

process.rivetAnalyzer.CrossSection = cms.double(1.582e+03)

## DIJET
## AlphaQCD:AlphaMZ
## default    0.113      0.123
## 1.431e+09  1.328e+09  1.341e+09
##
## ZPJ
## AlphaQCD:AlphaMZ
## default    0.113      0.123
## 1.582e+03  1.607e+03  1.615e+03
##
## UE
## AlphaQCD:AlphaMZ
## default    0.113      0.123      0.100      0.136
## 7.784e+10  7.784e+10  7.784e+10  7.784e+10  7.784e+10

process.rivetAnalyzer.UseExternalWeight = cms.bool(True)  # for weighted events
process.rivetAnalyzer.useGENweights = cms.bool(True)
process.rivetAnalyzer.useLHEweights = cms.bool(False)  # doesn't matter as no separate LHE generator

process.rivetAnalyzer.AnalysisNames = cms.vstring('CMS_2018_PAS_SMP_18_QGX_ZPJ')

## Substructure
## CMS_2018_PAS_SMP_18_QGX_ZPJ
## CMS_2018_PAS_SMP_18_QGX_DIJET
## Underlying events
## CMS_Internal_FSQ_15_007','CMS_FSQ_15_008','CMS_2015_I1384119','ATLAS_2016_I1419652','CMS_FSQ_15_005','CMS_FSQ_15_006

process.rivetAnalyzer.OutputFile = cms.string('DY_Herwig7_Nov3.yoda')

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion

print("Running with seed", process.RandomNumberGeneratorService.generator.initialSeed)

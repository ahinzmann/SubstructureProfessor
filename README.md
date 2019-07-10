# SubstructureProfessor

The following instructions are based on:
https://twiki.cern.ch/twiki/bin/viewauth/CMS/Rivet
https://twiki.cern.ch/twiki/bin/view/CMS/ProfessorTutorialForTuning

Setup your own fork of the Rivet GitLab repository:
* Go to https://gitlab.cern.ch/cms-gen/Rivet and press the fork button
* Then install CMSSW, Rivet and compile (see also README.md in repository):

cmsrel CMSSW_10_0_0

cd CMSSW_10_0_0/src

cmsenv

git-cms-init

git-cms-addpkg GeneratorInterface/RivetInterface

git-cms-addpkg Configuration/Generator

kinit ${USER}@CERN.CH

git clone https://:@gitlab.cern.ch:8443/${USER}/Rivet.git

source Rivet/rivetSetup.sh

scram b -j8

git clone git@github.com:ahinzmann/SubstructureProfessor.git

cd SubstructureProfessor

Adjust and run submitJobs.py to get the commands for tunings and comparisons

# Rivet plugins

For CMS jet charge, merge this into your fork: https://gitlab.cern.ch/hinzmann/Rivet/compare/master...SMP15003_datafix

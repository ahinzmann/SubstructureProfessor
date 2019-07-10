# SubstructureProfessor

The following instructions are based on:

https://twiki.cern.ch/twiki/bin/viewauth/CMS/Rivet

https://twiki.cern.ch/twiki/bin/view/CMS/ProfessorTutorialForTuning

Setup your own fork of the Rivet GitLab repository:
* Go to https://gitlab.cern.ch/cms-gen/Rivet and press the fork button
* Then install CMSSW, Rivet and compile (see also README.md in repository):

export SCRAM_ARCH=slc7_amd64_gcc630

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch

source $VO_CMS_SW_DIR/cmsset_default.sh

cmsrel CMSSW_10_0_0

cd CMSSW_10_0_0/src

cmsenv

git-cms-init

git-cms-addpkg GeneratorInterface/RivetInterface

git-cms-addpkg Configuration/Generator

kinit ${USER}@CERN.CH

git config --global http.emptyAuth true 

git clone https://:@gitlab.cern.ch:8443/${USER}/Rivet.git

source Rivet/rivetSetup.sh

scram b -j8

git clone git@github.com:ahinzmann/SubstructureProfessor.git

cd SubstructureProfessor

To get the commands for tunings and comparisons, adjust and run:

submitJobsPythia8.py

submitJobsHerwig7.py

analyse.py

# Rivet plugins

For CMS jet charge, merge this into your fork: https://gitlab.cern.ch/hinzmann/Rivet/compare/master...SMP15003_datafix

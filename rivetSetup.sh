#!/bin/bash
for GROUP in TOP FSQ SMP HIG SUS HIN EXO BPH B2G GEN
do
  export RIVET_REF_PATH=$RIVET_REF_PATH:$CMSSW_BASE/src/Rivet/${GROUP}/data
  export RIVET_DATA_PATH=$RIVET_DATA_PATH:$CMSSW_BASE/src/Rivet/${GROUP}/data
  export RIVET_INFO_PATH=$RIVET_INFO_PATH:$CMSSW_BASE/src/Rivet/${GROUP}/data
  export RIVET_PLOT_PATH=$RIVET_PLOT_PATH:$CMSSW_BASE/src/Rivet/${GROUP}/data
done

# cmsRivet scripts
export PATH=$PATH:$CMSSW_BASE/src/Rivet/scripts

# add latex package missing on lxplus7
export TEXMFHOME=$TEXMFHOME:$CMSSW_BASE/src/Rivet/texmf

which yodamerge &> /dev/null || GETYODA=1
if [ $GETYODA ]; then
  eval `scram tool info yoda | grep YODA_BASE`
  export PATH=$PATH:$YODA_BASE/bin
fi
